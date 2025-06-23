import { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [message, setMessage] = useState<string>('');
  const [reply, setReply] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/chat/', { message });
      setReply(response.data.reply);
    } catch (error) {
      console.error('Error:', error);
      setReply('Error getting response.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <h1 className="text-2xl font-bold mb-4">Ngamba Island Chatbot</h1>
      <form onSubmit={handleSubmit} className="flex flex-col w-full max-w-md space-y-4">
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask the chatbot..."
          className="p-2 border border-gray-300 rounded"
          required
        />
        <button
          type="submit"
          className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
          disabled={loading}
        >
          {loading ? 'Loading...' : 'Send'}
        </button>
      </form>
      {reply && (
        <div className="mt-4 p-4 bg-white border border-gray-300 rounded w-full max-w-md">
          <strong>Chatbot Reply:</strong>
          <p>{reply}</p>
        </div>
      )}
    </div>
  );
};

export default App;
