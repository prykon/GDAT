# GDAT - Google Dork Automated Tool

## Instructions:
1. Install requirements
```pip install -r requirements.txt```

2. Run the gdat.py script from a command line adding the parameter -u or --url with the target url

**Example:**
```python gdat.py -u example.com```

For better results, try not to limit the target url to the 'www' subdomain due to the fact that vulnerabilities could exist in other subdomains (eg. *admin.example.com*)