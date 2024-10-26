-- Core Tables
CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY,
    store_name TEXT NOT NULL,
    location TEXT NOT NULL,
    region TEXT NOT NULL,
    latitude DECIMAL(10,8),
    longitude DECIMAL(11,8),
    contact_number TEXT,
    email TEXT,
    opening_hours TEXT
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    description TEXT,
    base_price DECIMAL(10,2) NOT NULL,
    category TEXT NOT NULL,
    subcategory TEXT,
    manufacturer TEXT,
    min_stock_level INTEGER DEFAULT 0,
    seasonal_flag BOOLEAN DEFAULT FALSE,
    weather_sensitive BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inventory Management
CREATE TABLE inventory_snapshots (
    snapshot_id INTEGER PRIMARY KEY,
    store_id INTEGER,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    snapshot_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    stock_status TEXT CHECK (stock_status IN ('Low', 'Normal', 'Excess')),
    days_of_supply INTEGER,
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE inventory_transactions (
    transaction_id INTEGER PRIMARY KEY,
    store_id INTEGER,
    product_id INTEGER,
    transaction_type TEXT CHECK (transaction_type IN ('Inbound', 'Outbound', 'Adjustment')),
    quantity INTEGER NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reference_number TEXT,
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Enhanced Feedback System
CREATE TABLE feedback (
    feedback_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    store_id INTEGER,
    customer_id TEXT,
    feedback_text TEXT NOT NULL,
    --sentiment_score DECIMAL(3,2),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    feedback_source TEXT CHECK (source IN ('API', 'Website', 'Mobile App', 'In-Store')),
    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    satisfaction_level TEXT CHECK (satisfaction_level IN ('Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very Dissatisfied')),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE feedback_keywords (
    keyword_id INTEGER PRIMARY KEY,
    feedback_id INTEGER,
    keyword TEXT NOT NULL,
    keyword_type TEXT CHECK (keyword_type IN ('Feature', 'Issue', 'Sentiment', 'Product')),
    FOREIGN KEY (feedback_id) REFERENCES feedback(feedback_id)
);

-- Weather Tracking
CREATE TABLE weather_data (
    weather_id INTEGER PRIMARY KEY,
    store_id INTEGER,
    temperature DECIMAL(5,2),
    humidity DECIMAL(5,2),
    condition TEXT,
    precipitation DECIMAL(5,2),
    wind_speed DECIMAL(5,2),
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    forecast_date DATE,
    data_source TEXT,
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE weather_impact (
    impact_id INTEGER PRIMARY KEY,
    weather_id INTEGER,
    product_id INTEGER,
    impact_type TEXT CHECK (impact_type IN ('Positive', 'Negative', 'Neutral')),
    --impact_strength DECIMAL(3,2),
    notes TEXT,
    FOREIGN KEY (weather_id) REFERENCES weather_data(weather_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Enhanced Festival Calendar
CREATE TABLE festivals (
    festival_id INTEGER PRIMARY KEY,
    festival_name TEXT NOT NULL,
    region_id INTEGER,
    start_date DATE,
    end_date DATE,
    recurrence TEXT CHECK (recurrence IN ('Yearly', 'Monthly', 'One-time')),
    significance TEXT,
    data_source TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

CREATE TABLE festival_product_impact (
    impact_id INTEGER PRIMARY KEY,
    festival_id INTEGER,
    product_id INTEGER,
    impact_factor TEXT CHECK (impact_factor IN ('Positive', 'Negative', 'Neutral')),
    --estimated_demand_change DECIMAL(5,2),
    --historical_accuracy DECIMAL(3,2),
    notes TEXT,
    FOREIGN KEY (festival_id) REFERENCES festivals(festival_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Social Media and News Integration
CREATE TABLE social_media_trends (
    trend_id INTEGER PRIMARY KEY,
    trend_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    platform TEXT CHECK (platform IN ('Twitter', 'Instagram', 'Facebook', 'TikTok', 'LinkedIn')),
    trend_text TEXT NOT NULL,
    --sentiment DECIMAL(3,2),
    engagement_level INTEGER,
    reach INTEGER,
    --trend_score DECIMAL(5,2),
    verified_source BOOLEAN DEFAULT FALSE
);


CREATE TABLE market_impact (
    impact_id INTEGER PRIMARY KEY,
    source_type TEXT CHECK (source_type IN ('Social', 'News')),
    source_id INTEGER,
    product_id INTEGER,
    impact_description TEXT,
    impact_score DECIMAL(3,2),
    confidence_level DECIMAL(3,2),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Analysis Support Views
CREATE VIEW product_demand_factors AS
SELECT 
    p.product_id,
    p.product_name,
    i.quantity,
    w.condition as weather_condition,
    f.festival_name,
    smt.trend_score as social_trend_score,
    nf.relevance_score as news_relevance
FROM products p
LEFT JOIN inventory_snapshots i ON p.product_id = i.product_id
LEFT JOIN weather_impact wi ON p.product_id = wi.product_id
LEFT JOIN weather_data w ON wi.weather_id = w.weather_id
LEFT JOIN festival_product_impact fpi ON p.product_id = fpi.product_id
LEFT JOIN festivals f ON fpi.festival_id = f.festival_id
LEFT JOIN market_impact mi ON p.product_id = mi.product_id
LEFT JOIN social_media_trends smt ON mi.source_id = smt.trend_id
LEFT JOIN news_feed nf ON mi.source_id = nf.news_id
WHERE i.snapshot_date = CURRENT_DATE;

-- Indexes for Performance
CREATE INDEX idx_inventory_date ON inventory_snapshots(snapshot_date);
CREATE INDEX idx_weather_date ON weather_data(recorded_at);
CREATE INDEX idx_feedback_date ON feedback(feedback_date);
CREATE INDEX idx_social_trends_date ON social_media_trends(trend_date);
CREATE INDEX idx_news_date ON news_feed(publication_date);

-- Example of a time-series analysis view
CREATE VIEW product_timeline_analysis AS
SELECT 
    p.product_id,
    p.product_name,
    DATE(i.snapshot_date) as date,
    AVG(i.quantity) as avg_inventory,
    COUNT(f.feedback_id) as feedback_count,
    AVG(f.sentiment_score) as avg_sentiment,
    w.condition as weather_condition,
    GROUP_CONCAT(DISTINCT f.festival_name) as active_festivals,
    COUNT(DISTINCT smt.trend_id) as social_trends_count,
    COUNT(DISTINCT nf.news_id) as news_mentions_count
FROM products p
LEFT JOIN inventory_snapshots i ON p.product_id = i.product_id
LEFT JOIN feedback f ON p.product_id = f.product_id
LEFT JOIN weather_data w ON DATE(i.snapshot_date) = DATE(w.recorded_at)
LEFT JOIN festival_product_impact fpi ON p.product_id = fpi.product_id
LEFT JOIN festivals f ON fpi.festival_id = f.festival_id
LEFT JOIN market_impact mi ON p.product_id = mi.product_id
LEFT JOIN social_media_trends smt ON mi.source_id = smt.trend_id
LEFT JOIN news_feed nf ON mi.source_id = nf.news_id
GROUP BY p.product_id, DATE(i.snapshot_date);