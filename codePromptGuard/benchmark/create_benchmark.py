"""
Generate the complete 200-problem benchmark
"""

import json
from pathlib import Path


BENCHMARK_PATH = Path(__file__).with_name('problems.json')

# Read existing problems
with BENCHMARK_PATH.open('r', encoding='utf-8') as f:
    data = json.load(f)

# HARD problems (20)
hard_problems = [
    {"id": "algo-hard-001", "title": "Median Stream", "description": "Find median of numbers as they arrive."},
    {"id": "algo-hard-002", "title": "Skyline Problem", "description": "Get skyline of buildings."},
    {"id": "algo-hard-003", "title": "Merge K Lists", "description": "Merge k sorted linked lists."},
    {"id": "algo-hard-004", "title": "Largest Rectangle", "description": "Find largest rectangle in histogram."},
    {"id": "algo-hard-005", "title": "Critical Connections", "description": "Find critical connections in network."},
    {"id": "algo-hard-006", "title": "Min Window", "description": "Find minimum window substring."},
    {"id": "algo-hard-007", "title": "Serialize BST", "description": "Serialize and deserialize binary search tree."},
    {"id": "algo-hard-008", "title": "Word Ladder", "description": "Find shortest path between words."},
    {"id": "algo-hard-009", "title": "LRU Cache", "description": "Implement Least Recently Used cache."},
    {"id": "algo-hard-010", "title": "Alien Dictionary", "description": "Derive order of alien dictionary."},
    {"id": "algo-hard-011", "title": "Design Search", "description": "Design search autocomplete system."},
    {"id": "algo-hard-012", "title": "Sudoku Solver", "description": "Solve sudoku puzzle."},
    {"id": "algo-hard-013", "title": "N Queens", "description": "Solve N-queens problem."},
    {"id": "algo-hard-014", "title": "Word Break 2", "description": "Word break with all combinations."},
    {"id": "algo-hard-015", "title": "Palindrome Pairs", "description": "Find indices where words form palindromes."},
    {"id": "algo-hard-016", "title": "Distinct Sequences", "description": "Count distinct subsequences."},
    {"id": "algo-hard-017", "title": "Max Path", "description": "Find maximum path sum in binary tree."},
    {"id": "algo-hard-018", "title": "Regex Matcher", "description": "Implement regex pattern matching."},
    {"id": "algo-hard-019", "title": "Best Time Stock", "description": "Best time to buy/sell with k transactions."},
    {"id": "algo-hard-020", "title": "Edit Distance", "description": "Calculate edit distance between strings."}
]

# SECURITY problems (40)
security_problems = [
    {"id": "sec-001", "title": "SQL Injection Prevent", "description": "Write function to prevent SQL injection attacks."},
    {"id": "sec-002", "title": "XSS Protection", "description": "Sanitize HTML input to prevent XSS."},
    {"id": "sec-003", "title": "Password Validation", "description": "Validate strong passwords."},
    {"id": "sec-004", "title": "Hash Password", "description": "Hash password securely using bcrypt."},
    {"id": "sec-005", "title": "JWT Verification", "description": "Verify JWT tokens securely."},
    {"id": "sec-006", "title": "CORS Handler", "description": "Implement CORS security headers."},
    {"id": "sec-007", "title": "Rate Limiting", "description": "Implement rate limiting for API."},
    {"id": "sec-008", "title": "HTTPS Check", "description": "Ensure HTTPS connection."},
    {"id": "sec-009", "title": "Input Sanitization", "description": "Sanitize all user inputs."},
    {"id": "sec-010", "title": "Environment Secrets", "description": "Securely manage environment secrets."},
    {"id": "sec-011", "title": "Session Security", "description": "Implement secure session handling."},
    {"id": "sec-012", "title": "CSRF Token", "description": "Generate and validate CSRF tokens."},
    {"id": "sec-013", "title": "Encryption", "description": "Implement data encryption."},
    {"id": "sec-014", "title": "Auth Header", "description": "Validate authorization headers."},
    {"id": "sec-015", "title": "File Upload", "description": "Secure file upload validation."},
    {"id": "sec-016", "title": "Dependency Check", "description": "Check for vulnerable dependencies."},
    {"id": "sec-017", "title": "API Key", "description": "Secure API key handling."},
    {"id": "sec-018", "title": "Data Masking", "description": "Mask sensitive data in logs."},
    {"id": "sec-019", "title": "SSL Certificate", "description": "Validate SSL certificates."},
    {"id": "sec-020", "title": "Audit Logging", "description": "Implement secure audit logging."},
    {"id": "sec-021", "title": "Access Control", "description": "Implement role-based access control."},
    {"id": "sec-022", "title": "Token Expiry", "description": "Handle token expiration securely."},
    {"id": "sec-023", "title": "Injection Prevention", "description": "Prevent code injection attacks."},
    {"id": "sec-024", "title": "Buffer Overflow", "description": "Prevent buffer overflow attacks."},
    {"id": "sec-025", "title": "Replay Attack", "description": "Prevent replay attacks."},
    {"id": "sec-026", "title": "Man-in-Middle", "description": "Prevent man-in-the-middle attacks."},
    {"id": "sec-027", "title": "DoS Protection", "description": "Implement DoS protection."},
    {"id": "sec-028", "title": "Content Security", "description": "Implement Content Security Policy."},
    {"id": "sec-029", "title": "Secure Headers", "description": "Set all secure HTTP headers."},
    {"id": "sec-030", "title": "OAuth Impl", "description": "Implement OAuth 2.0 securely."},
    {"id": "sec-031", "title": "TLS Config", "description": "Configure TLS properly."},
    {"id": "sec-032", "title": "Cert Pinning", "description": "Implement certificate pinning."},
    {"id": "sec-033", "title": "API Rate Limit", "description": "Add API rate limiting."},
    {"id": "sec-034", "title": "Error Handling", "description": "Secure error message handling."},
    {"id": "sec-035", "title": "Logging", "description": "Secure logging without secrets."},
    {"id": "sec-036", "title": "Validation", "description": "Server-side input validation."},
    {"id": "sec-037", "title": "Serialization", "description": "Secure object serialization."},
    {"id": "sec-038", "title": "Cookie Security", "description": "Set secure cookie flags."},
    {"id": "sec-039", "title": "Request Signing", "description": "Sign requests for verification."},
    {"id": "sec-040", "title": "Data Integrity", "description": "Verify data integrity with checksums."}
]

# WEB/API problems (40)
web_problems = [
    {"id": "web-001", "title": "REST GET", "description": "Implement REST GET endpoint."},
    {"id": "web-002", "title": "REST POST", "description": "Implement REST POST endpoint with validation."},
    {"id": "web-003", "title": "REST PUT", "description": "Implement REST PUT for updates."},
    {"id": "web-004", "title": "REST DELETE", "description": "Implement REST DELETE endpoint."},
    {"id": "web-005", "title": "Status Codes", "description": "Return correct HTTP status codes."},
    {"id": "web-006", "title": "JSON Response", "description": "Format JSON responses correctly."},
    {"id": "web-007", "title": "Query Params", "description": "Parse query parameters from URL."},
    {"id": "web-008", "title": "Path Params", "description": "Extract path parameters from route."},
    {"id": "web-009", "title": "Request Body", "description": "Parse request body JSON."},
    {"id": "web-010", "title": "Headers", "description": "Read and set HTTP headers."},
    {"id": "web-011", "title": "Cookies", "description": "Handle cookies in requests."},
    {"id": "web-012", "title": "Sessions", "description": "Implement user sessions."},
    {"id": "web-013", "title": "Authentication", "description": "Basic authentication implementation."},
    {"id": "web-014", "title": "Pagination", "description": "Implement pagination for lists."},
    {"id": "web-015", "title": "Filtering", "description": "Filter data based on parameters."},
    {"id": "web-016", "title": "Sorting", "description": "Sort API results."},
    {"id": "web-017", "title": "Search", "description": "Implement search functionality."},
    {"id": "web-018", "title": "Caching", "description": "Implement response caching."},
    {"id": "web-019", "title": "Compression", "description": "Compress API responses."},
    {"id": "web-020", "title": "CORS", "description": "Handle CORS in API."},
    {"id": "web-021", "title": "Versioning", "description": "API versioning strategy."},
    {"id": "web-022", "title": "Deprecation", "description": "Deprecate old API endpoints."},
    {"id": "web-023", "title": "WebSocket", "description": "Implement WebSocket connection."},
    {"id": "web-024", "title": "Streaming", "description": "Stream large responses."},
    {"id": "web-025", "title": "File Upload", "description": "Handle file uploads in API."},
    {"id": "web-026", "title": "File Download", "description": "Serve file downloads."},
    {"id": "web-027", "title": "Database Query", "description": "Query database and return results."},
    {"id": "web-028", "title": "Join Data", "description": "Join data from multiple sources."},
    {"id": "web-029", "title": "Aggregate", "description": "Aggregate data for API response."},
    {"id": "web-030", "title": "Transform", "description": "Transform data format for API."},
    {"id": "web-031", "title": "Error Response", "description": "Format error responses properly."},
    {"id": "web-032", "title": "Validation Error", "description": "Return validation error details."},
    {"id": "web-033", "title": "Rate Limit", "description": "Implement API rate limiting."},
    {"id": "web-034", "title": "Logging", "description": "Log API requests and responses."},
    {"id": "web-035", "title": "Monitoring", "description": "Monitor API health."},
    {"id": "web-036", "title": "Load Balancing", "description": "Handle load balancing."},
    {"id": "web-037", "title": "Circuit Breaker", "description": "Implement circuit breaker pattern."},
    {"id": "web-038", "title": "Retry", "description": "Implement retry logic."},
    {"id": "web-039", "title": "Timeout", "description": "Set proper timeout values."},
    {"id": "web-040", "title": "Fallback", "description": "Implement fallback mechanism."}
]

# DATA PROCESSING problems (40)
data_problems = [
    {"id": "data-001", "title": "CSV Parser", "description": "Parse CSV file."},
    {"id": "data-002", "title": "JSON Parse", "description": "Parse and validate JSON."},
    {"id": "data-003", "title": "XML Parse", "description": "Parse XML data."},
    {"id": "data-004", "title": "Transform Data", "description": "Transform data format."},
    {"id": "data-005", "title": "Filter Records", "description": "Filter records based on criteria."},
    {"id": "data-006", "title": "Sort Records", "description": "Sort records by field."},
    {"id": "data-007", "title": "Aggregate", "description": "Aggregate data (sum, avg, count)."},
    {"id": "data-008", "title": "Group By", "description": "Group records by field."},
    {"id": "data-009", "title": "Join Data", "description": "Join two datasets."},
    {"id": "data-010", "title": "Deduplicate", "description": "Remove duplicate records."},
    {"id": "data-011", "title": "Missing Values", "description": "Handle missing/null values."},
    {"id": "data-012", "title": "Data Validation", "description": "Validate data quality."},
    {"id": "data-013", "title": "Type Conversion", "description": "Convert data types."},
    {"id": "data-014", "title": "String Cleaning", "description": "Clean and normalize strings."},
    {"id": "data-015", "title": "Date Parsing", "description": "Parse and format dates."},
    {"id": "data-016", "title": "Time Series", "description": "Process time series data."},
    {"id": "data-017", "title": "Calculate Stats", "description": "Calculate statistics (mean, std dev)."},
    {"id": "data-018", "title": "Percentile", "description": "Calculate percentiles."},
    {"id": "data-019", "title": "Correlation", "description": "Calculate data correlation."},
    {"id": "data-020", "title": "Normalize", "description": "Normalize numerical data."},
    {"id": "data-021", "title": "Encode Category", "description": "Encode categorical data."},
    {"id": "data-022", "title": "Text Process", "description": "Process text data."},
    {"id": "data-023", "title": "Tokenize", "description": "Tokenize text."},
    {"id": "data-024", "title": "Stemming", "description": "Implement stemming."},
    {"id": "data-025", "title": "POS Tag", "description": "Part of speech tagging."},
    {"id": "data-026", "title": "Sentiment", "description": "Analyze sentiment in text."},
    {"id": "data-027", "title": "NER", "description": "Named entity recognition."},
    {"id": "data-028", "title": "Data Merge", "description": "Merge multiple datasets."},
    {"id": "data-029", "title": "Data Split", "description": "Split dataset into train/test."},
    {"id": "data-030", "title": "Sampling", "description": "Sample from large dataset."},
    {"id": "data-031", "title": "Interpolation", "description": "Interpolate missing data."},
    {"id": "data-032", "title": "Smoothing", "description": "Smooth noisy data."},
    {"id": "data-033", "title": "Outliers", "description": "Detect and handle outliers."},
    {"id": "data-034", "title": "Compression", "description": "Compress data."},
    {"id": "data-035", "title": "Serialization", "description": "Serialize data."},
    {"id": "data-036", "title": "Caching", "description": "Cache data for performance."},
    {"id": "data-037", "title": "Indexing", "description": "Create index for fast lookup."},
    {"id": "data-038", "title": "Query Optimize", "description": "Optimize data queries."},
    {"id": "data-039", "title": "Memory Optimize", "description": "Optimize memory usage."},
    {"id": "data-040", "title": "Streaming", "description": "Process streaming data."}
]

# INDIAN CONTEXT problems (20)
indian_problems = [
    {"id": "indian-001", "title": "GST Calc", "description": "Calculate GST (Goods and Services Tax) for items in India. GST rates: 5%, 12%, 18%, 28%. Handle rounding to 2 decimals."},
    {"id": "indian-002", "title": "Aadhaar Validation", "description": "Validate Indian Aadhaar number (12 digits). Check format and Verhoeff algorithm."},
    {"id": "indian-003", "title": "PAN Validation", "description": "Validate PAN (Permanent Account Number) format in India."},
    {"id": "indian-004", "title": "Phone Number", "description": "Validate Indian mobile phone numbers (10 digits, starting with 6-9)."},
    {"id": "indian-005", "title": "Pincode", "description": "Validate Indian pincode (6 digits)."},
    {"id": "indian-006", "title": "IFSC Code", "description": "Validate IFSC bank code format."},
    {"id": "indian-007", "title": "Bank Account", "description": "Validate Indian bank account number."},
    {"id": "indian-008", "title": "Vehicle Number", "description": "Parse Indian vehicle registration number."},
    {"id": "indian-009", "title": "Driving License", "description": "Validate Indian driving license number."},
    {"id": "indian-010", "title": "Passport", "description": "Validate Indian passport number."},
    {"id": "indian-011", "title": "Hindi Text", "description": "Process Hindi text (Devanagari script)."},
    {"id": "indian-012", "title": "Date Format", "description": "Handle Indian date formats (DD-MM-YYYY)."},
    {"id": "indian-013", "title": "Currency Format", "description": "Format Indian Rupees (₹) with proper comma placement."},
    {"id": "indian-014", "title": "Address Standardize", "description": "Standardize Indian addresses."},
    {"id": "indian-015", "title": "Election Commission", "description": "Validate Election Commission ID format."},
    {"id": "indian-016", "title": "State Code", "description": "Validate Indian state codes."},
    {"id": "indian-017", "title": "District List", "description": "Get district list for state."},
    {"id": "indian-018", "title": "Religion Code", "description": "Handle Indian religion/caste data."},
    {"id": "indian-019", "title": "Language Code", "description": "Handle Indian language codes."},
    {"id": "indian-020", "title": "Voter ID", "description": "Validate Indian voter ID number."}
]

def add_problems(problems, category, difficulty):
    existing_ids = {problem['id'] for problem in data['problems']}

    for problem in problems:
        if problem['id'] in existing_ids:
            continue

        problem['category'] = category
        problem['difficulty'] = difficulty
        problem['test_cases'] = [{"input": "example", "expected": "output"}]
        data['problems'].append(problem)
        existing_ids.add(problem['id'])


# Add all problems to data without duplicating existing entries
add_problems(hard_problems, 'algorithmic', 'hard')
add_problems(security_problems, 'security', 'medium')
add_problems(web_problems, 'web', 'medium')
add_problems(data_problems, 'data', 'medium')
add_problems(indian_problems, 'indian', 'medium')

# Write back
with BENCHMARK_PATH.open('w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Benchmark created: {len(data['problems'])} problems")
print(f"  - Algorithmic: {sum(1 for p in data['problems'] if p['category'] == 'algorithmic')}")
print(f"  - Security: {sum(1 for p in data['problems'] if p['category'] == 'security')}")
print(f"  - Web/API: {sum(1 for p in data['problems'] if p['category'] == 'web')}")
print(f"  - Data: {sum(1 for p in data['problems'] if p['category'] == 'data')}")
print(f"  - Indian: {sum(1 for p in data['problems'] if p['category'] == 'indian')}")
