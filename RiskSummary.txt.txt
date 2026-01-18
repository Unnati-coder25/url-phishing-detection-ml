const RiskSummary = ({ result }) => (
  <div className="bg-slate-50 p-6 rounded mb-6">
    <h2 className="text-xl font-bold">Risk Level: {result.riskLevel}</h2>
    <p>Score: {result.riskScore}/100</p>
    <p>Domain: {result.domain}</p>
  </div>
);

export default RiskSummary;
