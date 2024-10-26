Shivam, [26-10-2024 14:16]
import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DataIntegrationSystem:
    def __init__(self, db_path: str, weather_api_key: str):
        """
        Initialize the data integration system.
        
        Args:
            db_path: Path to SQLite database
            weather_api_key: OpenWeatherMap API key
        """
        self.db_path = db_path
        self.weather_api_key = weather_api_key
        self.weather_base_url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
        self.news_base_url = 'https://news.google.com/rss/search'
        
        try:
            self.conn = sqlite3.connect(db_path)
            self.conn.row_factory = sqlite3.Row
            logger.info("Database connection established successfully")
        except sqlite3.Error as e:
            logger.error(f"Database connection error: {e}")
            raise

    def fetch_store_info(self, store_id: int) -> Dict:
        """Fetch store information from database"""
        try:
            query = """
                SELECT store_id, store_name, location, region
                FROM stores
                WHERE store_id = ?
            """
            cursor = self.conn.execute(query, (store_id,))
            result = cursor.fetchone()
            if result is None:
                raise ValueError(f"No store found with ID {store_id}")
            return dict(result)
        except sqlite3.Error as e:
            logger.error(f"Error fetching store info: {e}")
            raise

    def fetch_weather_forecast(self, region: str) -> Optional[Dict]:
        """Fetch 7-day weather forecast from OpenWeatherMap API"""
        try:
            params = {
                'q': f"{region},IN",
                'cnt': 7,
                'appid': self.weather_api_key,
                'units': 'metric'
            }
            response = requests.get(self.weather_base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching weather data: {e}")
            return None

    def fetch_news_headlines(self, region: str, product: str) -> Optional[List[Dict]]:
        """Fetch news headlines from Google News RSS"""
        try:
            params = {
                'q': f"{product} {region}",
                'gl': 'IN',
                'ceid': 'IN:en'
            }
            response = requests.get(self.news_base_url, params=params)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'xml')
            articles = soup.find_all('item')
            
            return [{
                'headline': article.title.text,
                'link': article.link.text,
                'publication_date': article.pubDate.text
            } for article in articles[:10]]  # Limit to 10 most recent articles
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching news headlines: {e}")
            return None
        except Exception as e:
            logger.error(f"Error parsing news data: {e}")
            return None

    def fetch_inventory_data(self, store_id: int) -> List[Dict]:
        """Fetch inventory data from database"""
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
        return [dict(row) for row

Shivam, [26-10-2024 14:16]
) for row in cursor.fetchall()]

    def fetch_feedback_analysis(self, store_id: int) -> List[Dict]:
        """Fetch customer feedback analysis from database"""
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

    def fetch_festival_data(self, store_id: int) -> List[Dict]:
        """Fetch upcoming festival data from database"""
        query = """
            SELECT 
                f.festival_name,
                f.start_date,
                f.end_date,
                f.significance,
                fpi.product_id,
                fpi.impact_factor
            FROM festivals f
            JOIN festival_product_impact fpi ON f.festival_id = fpi.festival_id
            JOIN stores s ON s.region = f.region_id
            WHERE s.store_id = ?
            AND f.start_date >= date('now')
            AND f.start_date <= date('now', '+30 days')
        """
        cursor = self.conn.execute(query, (store_id,))
        return [dict(row) for row in cursor.fetchall()]

    def fetch_social_trends(self) -> List[Dict]:
        """Fetch social media trends from database"""
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

    def integrate_data(self, store_id: int) -> Dict:
        """
        Integrate all data sources into a single JSON object.
        
        Args:
            store_id: Store ID to fetch data for
            
        Returns:
            Dictionary containing all integrated data
        """
        try:
            # Fetch store information first
            store_info = self.fetch_store_info(store_id)
            region = store_info['region']
            
            # Fetch data from all sources
            weather_data = self.fetch_weather_forecast(region)
            news_data = self.fetch_news_headlines(region, "Retail")  # Can be customized based on store type
            inventory_data = self.fetch_inventory_data(store_id)
            feedback_data = self.fetch_feedback_analysis(store_id)
            festival_data = self.fetch_festival_data(store_id)
            social_trends = self.fetch_social_trends()

            # Integrate all data into a single structure
            integrated_data = {
                "metadata": {
                    "store_id": store_id,
                    "timestamp": datetime.now().isoformat(),
                    "data_version": "1.0"
                },
                "store_info": store_info,
                "weather_forecast": weather_data.get('list', []) if weather_data else [],
                "market_insights": {
                    "news_headlines": news_data if news_data else [],
                    "social_trends": social_trends
                },
                "inventory_status": inventory_data,
                "customer_feedback": feedback_data,
                "upcoming_festivals": festival_data,
                "regional_context": {
                    "region": region,
                    "weather_alerts": self._extract_weather_alerts(weather_data) if weather_data else [],
                    "festival_impact":

Shivam, [26-10-2024 14:16]
self._summarize_festival_impact(festival_data)
                }
            }

            return integrated_data

        except Exception as e:
            logger.error(f"Error in data integration: {e}")
            raise

    def _extract_weather_alerts(self, weather_data: Dict) -> List[Dict]:
        """Extract relevant weather alerts from forecast data"""
        alerts = []
        if weather_data and 'list' in weather_data:
            for day in weather_data['list']:
                if day.get('weather', [{}])[0].get('main') in ['Rain', 'Snow', 'Extreme']:
                    alerts.append({
                        'date': datetime.fromtimestamp(day['dt']).isoformat(),
                        'condition': day['weather'][0]['main'],
                        'description': day['weather'][0]['description'],
                        'severity': 'high' if day['weather'][0]['main'] == 'Extreme' else 'medium'
                    })
        return alerts

    def _summarize_festival_impact(self, festival_data: List[Dict]) -> Dict:
        """Summarize festival impact on business"""
        return {
            'total_festivals': len(festival_data),
            'high_impact_festivals': [
                {
                    'name': festival['festival_name'],
                    'date': festival['start_date'],
                    'impact_factor': festival['impact_factor']
                }
                for festival in festival_data
                if float(festival['impact_factor']) > 0.7
            ]
        }

    def close(self):
        """Close database connection"""
        if hasattr(self, 'conn'):
            self.conn.close()
            logger.info("Database connection closed")

def main(store_id: int, db_path: str, weather_api_key: str):
    """
    Main function to run the data integration system.
    
    Args:
        store_id: Store ID to fetch data for
        db_path: Path to SQLite database
        weather_api_key: OpenWeatherMap API key
    """
    integrator = None
    try:
        integrator = DataIntegrationSystem(db_path, weather_api_key)
        integrated_data = integrator.integrate_data(store_id)
        
        # Print or return the integrated data
        return integrated_data
        
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
        raise
    finally:
        if integrator:
            integrator.close()

if name == "__main__":
    # Configuration
    STORE_ID = 1  # Replace with desired store ID
    DB_PATH = "database.db"  # Replace with your database path
    WEATHER_API_KEY = "your_openweathermap_api_key"  # Replace with your API key
    
    try:
        result = main(STORE_ID, DB_PATH, WEATHER_API_KEY)
        print(f"Data integration completed successfully for store {STORE_ID}")
    except Exception as e:
        logger.error(f"Application failed: {e}")
