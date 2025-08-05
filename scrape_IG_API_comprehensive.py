import requests
import json
from datetime import datetime

class InstagramGraphAPI:
    """
    Instagram Graph API Implementation (Definitive Version)
    - Fetches maximum data including total_interactions and shares.
    - Gracefully handles errors for metrics on older posts.
    - Provides comprehensive data structures.
    """
    
    def __init__(self, access_token, instagram_business_account_id):
        self.access_token = access_token
        self.instagram_business_account_id = instagram_business_account_id
        self.base_url = "https://graph.facebook.com/v19.0" 
        
    def get_account_info(self):
        """Get basic account information"""
        url = f"{self.base_url}/{self.instagram_business_account_id}"
        params = {
            'fields': 'username,name,profile_picture_url,followers_count,follows_count,media_count',
            'access_token': self.access_token
        }
        response = requests.get(url, params=params)
        return self._handle_response(response)
        
    def get_media_list(self, limit=25):
        """Get list of media posts including like/comment counts and media_url"""
        url = f"{self.base_url}/{self.instagram_business_account_id}/media"
        params = {
            # ADDED: media_url is back in the list
            'fields': 'id,caption,media_type,media_url,permalink,timestamp,username,like_count,comments_count',
            'limit': limit,
            'access_token': self.access_token
        }
        response = requests.get(url, params=params)
        return self._handle_response(response)
    
    def get_media_insights(self, media_id):
        """
        Get insights for a specific media post, gracefully handling missing metrics.
        """
        # ADDED: total_interactions and shares are back in the list
        all_possible_metrics = ['views', 'reach', 'saved', 'likes', 'comments', 'shares', 'total_interactions']
        
        formatted_insights = {}

        # We will request metrics one by one to handle errors gracefully.
        for metric in all_possible_metrics:
            url = f"{self.base_url}/{media_id}/insights"
            params = {
                'metric': metric,
                'access_token': self.access_token
            }
            response = requests.get(url, params=params)
            insight_data = self._handle_response(response, supress_error_print=True)

            if insight_data and 'data' in insight_data and insight_data['data']:
                # If successful, get the value
                value = insight_data['data'][0].get('values', [{}])[0].get('value', 0)
                formatted_insights[metric] = value
            else:
                # If it fails (e.g., 'shares' on an old post), mark as Not Available
                formatted_insights[metric] = "Not Available"

        return formatted_insights
    
    def get_media_details(self, media_id):
        """Get detailed information about a specific media post"""
        url = f"{self.base_url}/{media_id}"
        params = {
            # ADDED: media_url is back in the list
            'fields': 'id,caption,media_type,media_url,permalink,timestamp,username,like_count,comments_count,ig_id',
            'access_token': self.access_token
        }
        response = requests.get(url, params=params)
        return self._handle_response(response)
    
    def get_comprehensive_post_analytics(self, media_id):
        """
        Get comprehensive analytics for a specific post by its ID.
        """
        post_details = self.get_media_details(media_id)
        if not post_details: 
            return None
        
        insights = self.get_media_insights(media_id)
        
        comprehensive_data = {
            'post_details': post_details,
            'insights': insights if insights else "Insights could not be fetched.",
            'summary': {
                'likes': post_details.get('like_count', 0),
                'comments': post_details.get('comments_count', 0),
                'views': insights.get('views', 0) if insights else 0,
                'reach': insights.get('reach', 0) if insights else 0,
                'saved': insights.get('saved', 0) if insights else 0,
                'shares': insights.get('shares', 0) if insights else 0,
                'total_interactions': insights.get('total_interactions', 0) if insights else 0,
            }
        }
        
        return comprehensive_data

    def _handle_response(self, response, supress_error_print=False):
        """Handle API response and errors"""
        if response.status_code == 200:
            return response.json()
        
        if not supress_error_print:
            try:
                error_data = response.json()
                error_message = error_data.get('error', {}).get('message', 'No error message provided.')
                print(f"API Error ({response.status_code}): {error_message}")
            except json.JSONDecodeError:
                print(f"API Error ({response.status_code}): {response.text}")
        return None

def setup_instagram_api():
    """Replace with your actual credentials."""
    ACCESS_TOKEN = "EAAJsRK4bgtYBO2HZCuISvcl**************************GVMQWe4oVt2Tnt4wE0XTPefsKH9V26dH4qcu9hKobsip7dOUcpHZAiklDSBqZBn41pqtcqGlbem2EQsxR"
    INSTAGRAM_BUSINESS_ACCOUNT_ID = "178414754******932"
    
    if not ACCESS_TOKEN or not INSTAGRAM_BUSINESS_ACCOUNT_ID:
        print("!!! ERROR: Credentials are not set in setup_instagram_api() !!!")
        return None
    return InstagramGraphAPI(ACCESS_TOKEN, INSTAGRAM_BUSINESS_ACCOUNT_ID)

if __name__ == "__main__":
    print("Instagram Graph API Analytics Fetcher")
    print("=" * 50)
    
    api = setup_instagram_api()
    terminal_log_data = {} # Dictionary to hold all terminal output for saving

    if api:
        # 1. Get and print Account Info
        print("\nFetching Account Info...")
        account_info = api.get_account_info()
        if account_info:
            print(json.dumps(account_info, indent=2))
            terminal_log_data['account_info'] = account_info

        # 2. Get and print Media List
        print("\nFetching Recent Media (with like/comment counts)...")
        media_list = api.get_media_list(limit=10)
        if media_list:
            print(json.dumps(media_list, indent=2))
            terminal_log_data['media_list'] = media_list
        
        # 3. Get and print Comprehensive Analytics for all posts
        if media_list and 'data' in media_list:
            all_posts_analytics = []
            print("\n\n--- Comprehensive Analytics for all posts ---")
            
            for post in media_list['data']:
                post_analytics = api.get_comprehensive_post_analytics(post['id'])
                if post_analytics:
                    all_posts_analytics.append(post_analytics)
            
            # Print the final list to the terminal
            print(json.dumps(all_posts_analytics, indent=4))
            terminal_log_data['comprehensive_analytics'] = all_posts_analytics

            # 4. Save the files
            # Save the file with only the comprehensive analytics
            with open("instagram_analytics.json", 'w') as f:
                json.dump(all_posts_analytics, f, indent=4)
            print("\n==================================================")
            print(f"SUCCESS: Comprehensive analytics saved to instagram_analytics.json")
            
            # Save the file with ALL data that was printed
            with open("instagram_analytics_all_data.json", 'w') as f:
                json.dump(terminal_log_data, f, indent=4)
            print(f"SUCCESS: Full terminal log saved to instagram_analytics_all_data.json")
            print("==================================================")

        else:
            print("\nCould not find any media to analyze.")
    else:

        print("\nAPI initialization failed. Please check your credentials.")
