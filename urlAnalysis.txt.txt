export const analyzeURLLogic = (inputUrl) => {
  try {
    let urlToAnalyze = inputUrl.trim();
    if (!urlToAnalyze.startsWith('http')) {
      urlToAnalyze = 'https://' + urlToAnalyze;
    }

    const urlObj = new URL(urlToAnalyze);
    const checks = [];
    let riskScore = 0;

    const suspiciousTLDs = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz'];
    const legitimateDomains = ['google.com', 'facebook.com', 'paypal.com'];

    if (/^(\d{1,3}\.){3}\d{1,3}$/.test(urlObj.hostname)) {
      checks.push({ name: 'IP Address Used', status: 'danger', points: 25 });
      riskScore += 25;
    }

    if (suspiciousTLDs.some(tld => urlObj.hostname.endsWith(tld))) {
      checks.push({ name: 'Suspicious TLD', status: 'warning', points: 20 });
      riskScore += 20;
    }

    let riskLevel = riskScore < 25 ? 'Low Risk' :
                    riskScore < 50 ? 'Medium Risk' :
                    riskScore < 75 ? 'High Risk' : 'Critical Risk';

    return {
      url: urlToAnalyze,
      domain: urlObj.hostname,
      riskScore,
      riskLevel,
      checks
    };
  } catch {
    return { error: true, message: 'Invalid URL format' };
  }
};
