Feature Extraction Module for URL Phishing Detection
Extracts various features from URLs to train ML models
"""

import re
from urllib.parse import urlparse

class URLFeatureExtractor:
    """Extract features from URLs for phishing detection"""
    
    # List of suspicious keywords commonly found in phishing URLs
    SUSPICIOUS_KEYWORDS = [
        'secure', 'account', 'update', 'login', 'verify', 'banking',
        'confirm', 'password', 'suspend', 'alert', 'security'
    ]
    
    def __init__(self):
        """Initialize the feature extractor"""
        pass
    
    def extract_features(self, url):
        """
        Extract all features from a single URL
        
        Args:
            url (str): The URL to analyze
            
        Returns:
            dict: Dictionary containing all extracted features
        """
        features = {}
        
        # Parse the URL into components
        parsed = urlparse(url)
        
        # Feature 1: URL Length
        # Phishing URLs are often longer to hide malicious content
        features['url_length'] = len(url)
        
        # Feature 2: Number of dots
        # Multiple dots can indicate subdomain spoofing
        features['num_dots'] = url.count('.')
        
        # Feature 3: Has @ symbol
        # @ symbol can be used to hide the real domain
        features['has_at'] = 1 if '@' in url else 0
        
        # Feature 4: Has dash in domain
        # Dashes in domain names can be suspicious
        domain = parsed.netloc
        features['has_dash'] = 1 if '-' in domain else 0
        
        # Feature 5: Has double slash in path
        # Double slashes in path (not protocol) are suspicious
        path = parsed.path
        features['has_double_slash'] = 1 if '//' in path else 0
        
        # Feature 6: Uses HTTPS
        # Legitimate sites usually use HTTPS
        features['is_https'] = 1 if parsed.scheme == 'https' else 0
        
        # Feature 7: Number of subdomains
        # Too many subdomains can be suspicious
        if domain:
            # Remove port if present
            domain_parts = domain.split(':')[0].split('.')
            # Subtract 2 for main domain and TLD
            features['num_subdomains'] = max(0, len(domain_parts) - 2)
        else:
            features['num_subdomains'] = 0
        
        # Feature 8: Has suspicious keywords
        # Check if URL contains common phishing words
        url_lower = url.lower()
        features['has_suspicious_keyword'] = 1 if any(
            keyword in url_lower for keyword in self.SUSPICIOUS_KEYWORDS
        ) else 0
        
        # Feature 9: Has IP address instead of domain
        # Using IP address instead of domain name is suspicious
        features['has_ip'] = 1 if self._is_ip_address(domain) else 0
        
        # Feature 10: Ratio of digits to characters
        # High proportion of digits can be suspicious
        num_digits = sum(c.isdigit() for c in url)
        features['digit_ratio'] = num_digits / len(url) if len(url) > 0 else 0
        
        return features
    
    def _is_ip_address(self, domain):
        """
        Check if domain is an IP address
        
        Args:
            domain (str): Domain name to check
            
        Returns:
            bool: True if domain is an IP address
        """
        # Remove port if present
        domain = domain.split(':')[0]
        
        # Simple regex for IPv4 address
        ip_pattern = r'^(d{1,3}.){3}d{1,3}$'
        return bool(re.match(ip_pattern, domain))
    
    def extract_features_batch(self, urls):
        """
        Extract features from multiple URLs
        
        Args:
            urls (list): List of URLs to process
            
        Returns:
            list: List of feature dictionaries
        """
        return [self.extract_features(url) for url in urls]


# Test the feature extractor if run directly
if __name__ == "__main__":
    # Create feature extractor instance
    extractor = URLFeatureExtractor()
    
    # Test URLs
    test_urls = [
        "https://www.google.com",
        "http://secure-paypal-login.000webhostapp.com",
        "http://192.168.1.1/login"
    ]
    
    print("Testing Feature Extraction:")
    print("=" * 60)
    
    for url in test_urls:
        print(f"
URL: {url}")
        features = extractor.extract_features(url)
        for feature_name, value in features.items():
            print(f"  {feature_name}: {value}")
