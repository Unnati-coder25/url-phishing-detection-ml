import React, { useState } from 'react';
import { Shield } from 'lucide-react';
import { analyzeURLLogic } from '../utils/urlAnalysis';
import UrlInput from './UrlInput';
import RiskSummary from './RiskSummary';
import SecurityChecks from './SecurityChecks';

const PhishingDetector = () => {
  const [url, setUrl] = useState('');
  const [result, setResult] = useState(null);
  const [analyzing, setAnalyzing] = useState(false);

  const handleAnalyze = (inputUrl) => {
    setAnalyzing(true);
    setTimeout(() => {
      const output = analyzeURLLogic(inputUrl);
      setResult(output);
      setAnalyzing(false);
    }, 800);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 p-6">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-8">
          <Shield className="w-12 h-12 text-blue-400 mx-auto mb-3" />
          <h1 className="text-4xl font-bold text-white">URL Phishing Detector</h1>
          <p className="text-slate-300">Analyze URLs for phishing risks</p>
        </div>

        <UrlInput url={url} setUrl={setUrl} analyzing={analyzing} onAnalyze={handleAnalyze} />
        {result && <RiskSummary result={result} />}
        {result && !result.error && <SecurityChecks checks={result.checks} />}
      </div>
    </div>
  );
};

export default PhishingDetector;
