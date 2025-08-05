
# Project Documentation: Instagram Graph API Analytics Scraper

## 1. Project Aim & Goal

The primary objective of this project was to develop a Python script capable of fetching detailed analytics data for an Instagram Business Account using the Instagram Graph API. The required data points included post-specific metrics like likes, comments, views, reach, and shares, as well as overall account information. The final goal was to have a robust, error-tolerant script that provides comprehensive output both in the terminal for real-time debugging and in structured JSON files for data storage and analysis.

---

## 2. Core Functionality of the Final Script

The final script successfully accomplishes the following tasks:
*   **Connects** to the Instagram Graph API using a valid Access Token and Business Account ID.
*   **Fetches Basic Account Info**, including username, follower/following counts, and total media count.
*   **Retrieves a List of Recent Media**, including the post's `media_url`, like count, and comment count directly in the list.
*   **Performs Deep Analysis on Each Post**, fetching a comprehensive set of insight metrics.
*   **Outputs All Data** to the terminal in a structured, human-readable format for immediate review.
*   **Generates Two Distinct JSON Files**:
    1.  `instagram_analytics.json`: Contains a clean list of the comprehensive analytics for each post, ideal for data processing.
    2.  `all_data_instagram_analytics.json`: A complete log of all data printed to the terminal (Account Info, Media List, and Comprehensive Analytics), serving as a full data archive of the script's run.

---

## 3. Key Features & Design Choices

The final script was built with the following key features in mind:

*   **Maximum Data Retrieval:** It attempts to fetch a wide range of modern metrics, including `views`, `reach`, `saved`, `likes`, `comments`, `shares`, and `total_interactions`.
*   **Robust Error Handling:** The script is designed to not fail even if the API cannot provide a specific metric for a given post (e.g., `shares` on an old photo). It handles this gracefully by marking the specific metric as `"Not Available"` and continuing, ensuring maximum data collection without interruption.
*   **Verbose and Readable Code:** The code intentionally uses explicit `for` loops and avoids complex one-liners (like comprehensions) to maximize readability and make it easier to understand and maintain.
*   **Detailed Terminal Logging:** All major steps and fetched data are printed to the terminal, providing a clear, real-time view of the script's execution and simplifying the debugging process.
*   **Stable API Versioning:** The script uses a Long-Term Support (LTS) version of the Graph API (`v19.0`) to ensure stability and prevent unexpected breaking changes from newer, non-LTS versions.

---

## 4. Development Journey & Problems Solved

The development process involved overcoming several challenges to arrive at the final, robust solution.

### Challenge 1: Invalid API Fields & Metrics
> **Problem:** The initial code produced `(#100) nonexisting field` and `(#100) metric must be one of the following...` errors.
>
> **Analysis:** The script was requesting fields (`account_type`) and metrics (`engagement`) that were either named incorrectly or not available at the specified API endpoints.
>
> **Solution:** Corrected the field names and replaced conceptual metrics like `engagement` with available API metrics like `total_interactions`.

### Challenge 2: Deprecated Metrics
> **Problem:** A `(#100) impressions metric is no longer supported` error appeared as we moved to newer API versions.
>
> **Analysis:** Meta deprecated the `impressions` metric in favor of a new, unified `views` metric for all media types.
>
> **Solution:** The script was updated to request `views` instead of `impressions`, aligning it with modern API standards.

### Challenge 3: Inconsistent API Behavior & `Invalid parameter` Errors
> **Problem:** When requesting a full list of valid metrics at once, the API would sometimes return a generic `Invalid parameter` error, especially on older posts.
>
> **Analysis:** This was likely due to the API's inability to provide certain newer metrics (like `shares` or `total_interactions`) for older content. Instead of returning `0`, it would error out the entire request.
>
> **Solution:** The insight-fetching logic was re-engineered to request **each metric individually** in a loop. If a single metric fails, it is caught and marked as `"Not Available"`, allowing the script to successfully gather all other available data for that post.

### Challenge 4: Output and Usability
> **Problem:** The script needed to provide more detailed feedback during its run and create more useful, structured output files.
>
> **Solution:** The main execution block was designed to print each major data block (Account Info, Media List, and Comprehensive Analytics for all posts) to the terminal. Furthermore, logic was added to generate two separate, well-defined JSON files to serve different use cases (data analysis vs. full archival).

---

## 5. Prerequisites & Setup

To use this script, the following are required:

1.  An Instagram account converted to a **Business Account**.
2.  A Facebook Page connected to the Instagram Business Account.
3.  A Facebook App created on `developers.facebook.com` with the **Instagram Graph API** product added.
4.  A valid **User Access Token** generated from the Graph API Explorer with the following permissions:
    *   `instagram_basic`
    *   `instagram_manage_insights`
    *   `pages_read_engagement`
    *   `pages_show_list`
5.  The **Instagram Business Account ID**, which can be found by querying your Facebook Page ID.
6.  The `ACCESS_TOKEN` and `INSTAGRAM_BUSINESS_ACCOUNT_ID` must be correctly placed in the `setup_instagram_api()` function in the script.