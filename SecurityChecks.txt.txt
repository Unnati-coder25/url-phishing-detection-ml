const SecurityChecks = ({ checks }) => (
  <div>
    <h3 className="text-lg font-bold mb-3">Security Checks</h3>
    {checks.map((c, i) => (
      <div key={i} className="border p-3 rounded mb-2">
        {c.name} (+{c.points})
      </div>
    ))}
  </div>
);

export default SecurityChecks;
