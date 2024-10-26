import sqlite3
import json
from datetime import datetime, timedelta
import pandas as pd

class DataIntegrator:
    def __init__(self, db_path):
        """Initialize database connection"""
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def get_store_info(self, store_id):
        """Fetch store information"""
        query = """
        SELECT store_id, store_name, location, region
        FROM stores
        WHERE store_id = ?
        """
        cursor = self.conn.execute(query, (store_id,))
        return dict(cursor.fetchone())

    def get_inventory_data(self, store_id):
        """Fetch current inventory data"""
        query = """
        SELECT 
            p.product_id,
            p.product_name,
            p.category,
            p.subcategory,
            i.quantity,
            i.stock_status,
            i.days_of_supply
        FROM inventory_snapshots i
        JOIN products p ON i.product_id = p.product_id
        WHERE i.store_id = ?
        AND i.snapshot_date >= date('now', '-7 days')
        """
        cursor = self.conn.execute(query, (store_id,))
        return [dict(row) for row in cursor.fetchall()]

    def get_feedback_analysis(self, store_id):
        """Fetch customer feedback analysis"""
        query = """
        SELECT 
            f.product_id,
            p.product_name,
            COUNT(DISTINCT f.feedback_id) as feedback_count,
            GROUP_CONCAT(DISTINCT fk.keyword) as keywords
        FROM feedback f
        JOIN products p ON f.product_id = p.product_id
        LEFT JOIN feedback_keywords fk ON f.feedback_id = fk.feedback_id
        WHERE f.store_id = ?
        AND f.feedback_date >= date('now', '-30 days')
        GROUP BY f.product_id
        """
        cursor = self.conn.execute(query, (store_id,))
        return [dict(row) for row in cursor.fetchall()]

    def get_festival_data(self, store_id):
        """Fetch upcoming festival data"""
        query = """
        SELECT 
            f.festival_name,
            f.start_date,
            f.end_date,
            f.significance,
            fpi.product_id,
            fpi.impact_factor,
        FROM festivals f
        JOIN festival_product_impact fpi ON f.festival_id = fpi.festival_id
        JOIN stores s ON s.region = f.region_id
        WHERE s.store_id = ?
        AND f.start_date >= date('now')
        AND f.start_date <= date('now', '+30 days')
        """
        cursor = self.conn.execute(query, (store_id,))
        return [dict(row) for row in cursor.fetchall()]

    def get_social_trends(self, store_id):
        """Fetch relevant social media trends"""
        query = """
        SELECT 
            smt.platform,
            smt.trend_text,
            smt.engagement_level,
            mi.product_id,
            mi.impact_score
        FROM social_media_trends smt
        JOIN market_impact mi ON smt.trend_id = mi.source_id
        WHERE mi.source_type = 'Social'
        AND smt.trend_date >= date('now', '-7 days')
        """
        cursor = self.conn.execute(query)
        return [dict(row) for row in cursor.fetchall()]

    def integrate_data(self, store_id, weather_data, news_data):
        """Integrate all data sources into final JSON format"""
        store_info = self.get_store_info(store_id)
        inventory_data = self.get_inventory_data(store_id)
        feedback_data = self.get_feedback_analysis(store_id)
        festival_data = self.get_festival_data(store_id)
        social_trends = self.get_social_trends(store_id)

        integrated_data = {
            "store_info": store_info,
            "timestamp": datetime.now().isoformat(),
            "weather_forecast": weather_data["forecast"],
            "inventory_status": inventory_data,
            "customer_feedback": feedback_data,
            "upcoming_festivals": festival_data,
            "market_insights": {
                "news": news_data["news"],
                "social_trends": social_trends
            },
            "regional_context": {
                "region": store_info["region"],
                "local_weather_impact": self._analyze_weather_impact(weather_data, inventory_data),
                "cultural_events": self._summarize_festivals(festival_data)
            }
        }

        return integrated_data

    '''def _analyze_weather_impact(self, weather_data, inventory_data):
        """Analyze weather impact on inventory"""
        weather_impacts = []
        for forecast in weather_data["forecast"][:3]:  # Analysis for next 3 days
            impact = {
                "date": forecast["date"],
                "weather_condition": forecast["weather"],
                "affected_products": []
            }
            
            # Add logic to identify weather-sensitive products
            for product in inventory_data:
                if product["stock_status"] == "Low" and product.get("weather_sensitive", False):
                    impact["affected_products"].append({
                        "product_id": product["product_id"],
                        "product_name": product["product_name"],
                        "current_stock": product["quantity"],
                        "recommendation": "Consider weather forecast for restocking"
                    })
            
            weather_impacts.append(impact)
        return weather_impacts'''

    def _summarize_festivals(self, festival_data):
        """Summarize festival impact on inventory"""
        festival_summary = []
        for festival in festival_data:
            summary = {
                "festival_name": festival["festival_name"],
                "date_range": {
                    "start": festival["start_date"],
                    "end": festival["end_date"]
                },
                "significance": festival["significance"],
                "product_impact": {
                    "impact_factor": festival["impact_factor"],
                    "estimated_demand_change": float(festival["estimated_demand_change"])
                }
            }
            festival_summary.append(summary)
        return festival_summary

    def close(self):
        """Close database connection"""
        self.conn.close()

def main(store_id, db_path="retail_db.sqlite"):
    # Load sample weather and news data
    with open("weather_data.json", "r") as f:
        weather_data = json.load(f)
    
    with open("news_data.json", "r") as f:
        news_data = json.load(f)
    
    # Initialize data integrator
    integrator = DataIntegrator(db_path)
    
    try:
        # Generate integrated data
        integrated_data = integrator.integrate_data(store_id, weather_data, news_data)
        
        # Save to file
        output_filename = f"integrated_data_{store_id}_{datetime.now().strftime('%Y%m%d')}.json"
        with open(output_filename, "w", encoding="utf-8") as f:
            json.dump(integrated_data, f, ensure_ascii=False, indent=2)
        
        print(f"Data integration complete. Output saved to {output_filename}")
        
    finally:
        integrator.close()

if __name__ == "__main__":
    STORE_ID = 1  # Replace with desired store ID
    main(STORE_ID)