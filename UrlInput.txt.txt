import { Search } from 'lucide-react';

const UrlInput = ({ url, setUrl, analyzing, onAnalyze }) => (
  <form
    onSubmit={(e) => {
      e.preventDefault();
      onAnalyze(url);
    }}
    className="bg-white p-6 rounded-lg shadow mb-6"
  >
    <input
      value={url}
      onChange={(e) => setUrl(e.target.value)}
      placeholder="https://example.com"
      className="w-full border px-4 py-3 rounded mb-4"
    />
    <button
      disabled={analyzing}
      className="bg-blue-600 text-white px-6 py-2 rounded"
    >
      {analyzing ? 'Analyzing...' : 'Analyze'}
    </button>
  </form>
);

export default UrlInput;
