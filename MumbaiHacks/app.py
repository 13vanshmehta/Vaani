true = True
false = False
data1 = {
  "store_info": {
    "store_id": 1,
    "store_name": "Mumbai Central Store",
    "location": "Mumbai Central",
    "region": "Mumbai"
  },
  "timestamp": "2024-10-26T14:30:00Z",
  "weather_forecast": [
    {
      "date": "2024-10-26",
      "temperature": {
        "min": 26.5,
        "max": 31.0
      },
      "weather": "Clear",
      "humidity": 78,
      "wind_speed": 3.2,
      "description": "clear sky"
    },
    {
      "date": "2024-10-27",
      "temperature": {
        "min": 25.8,
        "max": 30.2
      },
      "weather": "Partly Cloudy",
      "humidity": 80,
      "wind_speed": 4.1,
      "description": "few clouds"
    }
  ],
  "inventory_status": [
    {
      "product_id": 101,
      "product_name": "Premium Umbrella",
      "category": "Accessories",
      "subcategory": "Rain Gear",
      "quantity": 45,
      "stock_status": "Low",
      "days_of_supply": 5,
      "weather_sensitive": true
    },
    {
      "product_id": 102,
      "product_name": "Cotton T-Shirt",
      "category": "Apparel",
      "subcategory": "Casual Wear",
      "quantity": 200,
      "stock_status": "Normal",
      "days_of_supply": 15,
      "weather_sensitive": false
    }
  ],
  "customer_feedback": [
    {
      "product_id": 101,
      "product_name": "Premium Umbrella",
      "avg_sentiment": 0.85,
      "feedback_count": 12,
      "keywords": ["durable", "quality", "expensive", "waterproof"],
      "feedback_examples": [
        {
          "text": "बहुत अच्छा छाता है, बारिश में काफी टिकाऊ है",
          "translated_text": "Very good umbrella, quite durable in rain",
          "language": "hindi",
          "sentiment_score": 0.92
        },
        {
          "text": "Good quality but slightly expensive",
          "language": "english",
          "sentiment_score": 0.78
        }
      ]
    }
  ],
  "upcoming_festivals": [
    {
      "festival_name": "Diwali",
      "date_range": {
        "start": "2024-11-01",
        "end": "2024-11-05"
      },
      "significance": "Festival of Lights",
      "product_impact": {
        "impact_factor": "Positive",
        "estimated_demand_change": 35.5,
        "affected_products": [
          {
            "product_id": 102,
            "product_name": "Cotton T-Shirt",
            "recommended_stock_increase": 50
          }
        ]
      }
    }
  ],
  "market_insights": {
    "news": [
      {
        "headline": "Mumbai Expects Heavy Rainfall Next Week",
        "link": "https://example.com/news/mumbai-rainfall",
        "publication_date": "2024-10-26T10:00:00Z",
        "relevance_score": 0.85,
        "products_affected": [101]
      },
      {
        "headline": "Festive Season Shopping Trends in Mumbai",
        "link": "https://example.com/news/festive-shopping",
        "publication_date": "2024-10-26T09:30:00Z",
        "relevance_score": 0.92,
        "products_affected": [102]
      }
    ],
    "social_trends": [
      {
        "platform": "Twitter",
        "trend_text": "#MumbaiRains trending with umbrella shortages",
        "sentiment": 0.45,
        "engagement_level": 8500,
        "product_id": 101,
        "impact_score": 0.75
      },
      {
        "platform": "Instagram",
        "trend_text": "#DiwaliShopping featuring casual wear",
        "sentiment": 0.88,
        "engagement_level": 12000,
        "product_id": 102,
        "impact_score": 0.82
      }
    ]
  },
  "regional_context": {
    "region": "Mumbai",
    "local_weather_impact": [
      {
        "date": "2024-10-26",
        "weather_condition": "Clear",
        "affected_products": [
          {
            "product_id": 101,
            "product_name": "Premium Umbrella",
            "current_stock": 45,
            "recommendation": "Consider weather forecast for restocking"
          }
        ]
      }
    ],
    "cultural_events": [
      {
        "festival_name": "Diwali",
        "cultural_significance": "Major shopping season",
        "recommended_actions": [
          {
            "action": "Increase casual wear inventory",
            "priority": "High",
            "timeline": "Next 7 days"
          }
        ]
      }
    ],
    "language_preferences": {
      "primary": "Marathi",
      "secondary": ["Hindi", "English"],
      "marketing_language_split": {
        "Marathi": 0.45,
        "Hindi": 0.35,
        "English": 0.20
      }
    }
  },
  "recommendations": {
    "inventory": [
      {
        "product_id": 101,
        "action": "Increase stock",
        "reasoning": "Low stock + upcoming rainfall forecast + high social media engagement",
        "urgency": "High",
        "recommended_quantity": 100
      }
    ],
    "marketing": [
      {
        "product_id": 102,
        "strategy": "Diwali promotion",
        "channels": ["Instagram", "Local stores"],
        "languages": ["Marathi", "Hindi"],
        "timing": "Start within 2 days"
      }
    ],
    "pricing": [
      {
        "product_id": 101,
        "action": "Maintain current price",
        "reasoning": "High demand due to weather forecast"
      }
    ]
  }
}

import json
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForSeq2SeqLM
import torch
import numpy as np
from datetime import datetime

# Secure HuggingFace auth token retrieval
HF_TOKEN = "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"

class RecommendationSystem:
    def __init__(self):
        # Initialize models with correct configurations
        self.lang_classifier = AutoModelForSequenceClassification.from_pretrained(
            "ai4bharat/indic-bert",
            use_auth_token=HF_TOKEN
        )
        self.sentiment_analyzer = AutoModelForSequenceClassification.from_pretrained(
            "ai4bharat/indic-bert",
            use_auth_token=HF_TOKEN
        )

        # Use correct tokenizer for translation model
        self.translator_tokenizer = AutoTokenizer.from_pretrained(
            "ai4bharat/indictrans2-en-indic-1B",
            use_auth_token=HF_TOKEN,
            src_lang="en",
            tgt_lang="hi"  # Default target language, can be changed
        )

        self.translator = AutoModelForSeq2SeqLM.from_pretrained(
            "ai4bharat/indictrans2-en-indic-1B",
            use_auth_token=HF_TOKEN
        )

        # Separate tokenizer for BERT-based models
        self.bert_tokenizer = AutoTokenizer.from_pretrained(
            "ai4bharat/indic-bert",
            use_auth_token=HF_TOKEN
        )

    def detect_language(self, text):
        """Detect language using IndicBERT"""
        inputs = self.bert_tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512  # Add explicit max_length
        )
        outputs = self.lang_classifier(**inputs)
        return torch.argmax(outputs.logits).item()

    def translate_to_english(self, text, source_lang):
        """Translate non-English text using IndicTrans v2"""
        if source_lang == "english":
            return text

        try:
            # Configure translation parameters
            inputs = self.translator_tokenizer(
                text,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=512
            )

            # Remove token_type_ids as it's not used by the translation model
            if 'token_type_ids' in inputs:
                del inputs['token_type_ids']

            # Generate translation with proper parameters
            outputs = self.translator.generate(
                **inputs,
                max_length=512,
                num_beams=4,
                length_penalty=1.0,
                early_stopping=True
            )

            return self.translator_tokenizer.decode(outputs[0], skip_special_tokens=True)
        except Exception as e:
            print(f"Translation error: {str(e)}")
            return text  # Return original text if translation fails

    def analyze_sentiment(self, text):
        """Analyze sentiment using IndicBERT"""
        inputs = self.bert_tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        )
        outputs = self.sentiment_analyzer(**inputs)
        sentiment_score = torch.sigmoid(outputs.logits).item()
        return sentiment_score

    def calculate_confidence_score(self, data_point):
        """Calculate confidence score based on multiple factors"""
        weights = {
            'sentiment': 0.3,
            'feedback_count': 0.2,
            'social_engagement': 0.25,
            'weather_relevance': 0.25
        }

        # Add error handling for missing or invalid values
        sentiment_score = max(0, min(1, data_point.get('avg_sentiment', 0.5)))
        feedback_count = max(0, min(1, data_point.get('feedback_count', 0) / 100))
        social_engagement = max(0, min(1, data_point.get('engagement_level', 0) / 10000))
        weather_relevance = 1.0 if data_point.get('weather_sensitive', False) else 0.5

        confidence_score = (
            weights['sentiment'] * sentiment_score +
            weights['feedback_count'] * feedback_count +
            weights['social_engagement'] * social_engagement +
            weights['weather_relevance'] * weather_relevance
        )

        return max(0, min(1, confidence_score))  # Ensure score is between 0 and 1

    def process_feedback(self, feedback_data):
        """Process customer feedback across languages"""
        processed_feedback = []

        try:
            for feedback in feedback_data:
                for example in feedback.get('feedback_examples', []):
                    # Input validation
                    if not isinstance(example, dict) or 'text' not in example:
                        continue

                    # Detect language if not specified
                    lang = example.get('language', self.detect_language(example['text']))

                    # Translate if not in English
                    english_text = self.translate_to_english(example['text'], lang)

                    # Analyze sentiment
                    sentiment = self.analyze_sentiment(english_text)

                    processed_feedback.append({
                        'original_text': example['text'],
                        'translated_text': english_text,
                        'language': lang,
                        'sentiment': sentiment
                    })
        except Exception as e:
            print(f"Error processing feedback: {str(e)}")
        print(processed_feedback)
        return processed_feedback

    def generate_recommendations(self, data):
        """Generate final recommendations based on all analyzed data"""
        recommendations = {
            'inventory': [],
            'campaigns': [],
            'market_predictions': []
        }

        try:
            # Process inventory recommendations with error handling
            for item in data.get('inventory_status', []):
                confidence_score = self.calculate_confidence_score({
                    'avg_sentiment': data.get('customer_feedback', [{}])[0].get('avg_sentiment', 0.5),
                    'feedback_count': data.get('customer_feedback', [{}])[0].get('feedback_count', 0),
                    'engagement_level': data.get('market_insights', {}).get('social_trends', [{}])[0].get('engagement_level', 0),
                    'weather_sensitive': item.get('weather_sensitive', False)
                })

                if confidence_score > 0.7:
                    if item.get('stock_status') == 'Low':
                        recommendations['inventory'].append({
                            'product_id': item.get('product_id'),
                            'product_name': item.get('product_name'),
                            'action': 'Increase stock immediately',
                            'confidence_score': confidence_score,
                            'reasoning': [
                                'Low current stock',
                                'High customer sentiment',
                                'Strong social media engagement'
                            ]
                        })

            # Process campaign recommendations
            for festival in data.get('upcoming_festivals', []):
                for product in festival.get('product_impact', {}).get('affected_products', []):
                    recommendations['campaigns'].append({
                        'product_id': product.get('product_id'),
                        'campaign_type': f"{festival.get('festival_name', 'Unknown')} Special",
                        'languages': data.get('regional_context', {}).get('language_preferences', {}).get('secondary', []),
                        'channels': ['Instagram', 'Local stores'],
                        'timing': f"Start before {festival.get('date_range', {}).get('start', 'TBD')}",
                        'confidence_score': 0.85
                    })

            # Process market predictions
            for trend in data.get('market_insights', {}).get('social_trends', []):
                recommendations['market_predictions'].append({
                    'product_id': trend.get('product_id'),
                    'trend': trend.get('trend_text'),
                    'prediction': 'Expected demand increase',
                    'confidence_score': trend.get('impact_score', 0.5),
                    'reasoning': [
                        f"High engagement on {trend.get('platform', 'social media')}",
                        'Positive sentiment analysis',
                        'Seasonal factors'
                    ]
                })

        except Exception as e:
            print(f"Error generating recommendations: {str(e)}")

        return recommendations

def main():
    try:
        # Initialize recommendation system
        recommender = RecommendationSystem()

        # Load sample data
        '''with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)'''
        data = data1

        # Process feedback
        processed_feedback = recommender.process_feedback(data['customer_feedback'])

        # Generate final recommendations
        recommendations = recommender.generate_recommendations(data)

        # Output formatted recommendations
        print(json.dumps(recommendations, indent=2, ensure_ascii=False))

    except Exception as e:
        print(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()