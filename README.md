# Instagram Business Analytics Extractor 📸

This project provides a powerful Python script to extract comprehensive analytics from your Instagram Business Account using the Instagram Graph API (via the Facebook Graph API). It gathers account information, media lists, and detailed post-level insights, including engagement metrics, reach, views, and more, with robust handling for unavailable data.

## 🚀 Project Overview

Understanding your Instagram performance is key to growing your audience and engagement. This tool automates the collection of critical data, transforming raw API responses into actionable insights for your social media strategy.

**Key Features:**
*   **Account Information:** Fetches essential details like username, follower count, and media count.
*   **Media List:** Retrieves recent posts with captions, media URLs, likes, and comments.
*   **Detailed Post Insights:** Collects metrics such as views, reach, saves, shares, and total interactions.
*   **Unavailable Metric Handling:** Gracefully indicates when specific metrics are not available for a post.
*   **Structured Data Output:** Generates clean JSON files for analytics and raw data archives.

## 🔗 Live Demonstration & Portfolio

For a comprehensive overview of the project, including its features, methodology, and results, please visit my portfolio:

*   **Instagram Analytics Portfolio:** [https://damilareadekeye.com/works/software/instagram-analytics/](https://damilareadekeye.com/works/software/instagram-analytics/)

## 📋 Features

*   **Account Metrics:**
    *   `username`, `name`, `profile_picture_url`
    *   `followers_count`, `follows_count`, `media_count`
*   **Media List (with basic engagement):**
    *   `id`, `caption`, `media_type`, `media_url`, `permalink`, `timestamp`, `username`
    *   `like_count`, `comments_count`
*   **Detailed Media Insights:** Fetches metrics per media item:
    *   `views`, `reach`, `saved`, `likes`, `comments`, `shares`, `total_interactions`
*   **Data Handling:** Marks unavailable metrics as `"Not Available"`.
*   **Output Files:** Creates `instagram_analytics.json` (comprehensive analytics) and `instagram_analytics_all_data.json` (raw data).

## 💡 Technologies & Tools

*   **Language:** Python 3.x
*   **API:** Instagram Graph API (via Facebook Graph API)
*   **Libraries:**
    *   `requests` for API interaction
    *   `json` for data processing
    *   `datetime` for timestamps
*   **Development Environment:** Visual Studio Code

## ⚙️ Getting Started

### Prerequisites

1.  **Python 3.x:** Must be installed on your system.
2.  **Instagram Business Account:** The account you want to analyze must be a Business Account.
3.  **Facebook Page Linked to Instagram:** Your Instagram Business Account must be linked to a Facebook Page.
4.  **Access Token:** A valid Access Token with necessary permissions (e.g., `instagram_basic`, `pages_show_list`, `instagram_manage_insights`).
5.  **Instagram Business Account ID:** The ID of your Instagram Business Account.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/damilarelekanadekeye/Instagram-Business-Analytics-Comprehensive-Media-Performance-Tracking.git
    cd Instagram-Business-Analytics-Comprehensive-Media-Performance-Tracking
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests
    ```

### Configuration

1.  **Edit `instagram_analytics.py`:**
    In the `setup_instagram_api()` function, replace the placeholder credentials:
    ```python
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN" # Replace with your Access Token please, mine is confidential.
    INSTAGRAM_BUSINESS_ACCOUNT_ID = "YOUR_INSTAGRAM_BUSINESS_ACCOUNT_ID" # Replace with your Instagram Business Account ID,  mine is confidential.
    ```

### Running the Script

Execute the script from your terminal:

```bash
python instagram_analytics.py
```

This will fetch the data and generate two JSON files:
*   `instagram_analytics.json`: Contains detailed analytics for each media item.
*   `instagram_analytics_all_data.json`: Stores all fetched data, including account info and raw media lists.

## ⚠️ Challenges & Solutions

*   **Metric Availability:** Certain metrics (e.g., 'shares') may not be available for all posts or older content. The script handles this by assigning `"Not Available"` to such metrics.
*   **API Permissions:** Ensuring the Access Token has the correct permissions is vital for successful data retrieval.
*   **Data Parsing:** Handling diverse data structures returned by the API requires careful parsing using methods like `.get()` to avoid errors from missing keys.

## 📈 Future Enhancements

*   **Automated Scheduling:** Set up regular data collection for continuous monitoring.
*   **Dashboard Integration:** Develop a web-based dashboard for interactive visualization of Instagram analytics.
*   **Content Strategy Insights:** Incorporate sentiment analysis for comments and identify top-performing content themes.
*   **Story & Reel Analytics:** Extend functionality to include analytics for Instagram Stories and Reels.

## 🤝 Contribution & Support

Contributions, feature requests, and bug reports are welcome! Please feel free to open an issue or submit a pull request.

---

_Connect with me on [LinkedIn](https://www.linkedin.com/in/damilareadekeye/) | Visit my [Portfolio](https://damilareadekeye.com)_
