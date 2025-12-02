const BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const getHeaders = () => {
  const headers = {
    'Content-Type': 'application/json',
  };
  const token = localStorage.getItem('jwt_token');
  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }
  return headers;
};

const handleResponse = async (response) => {
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'API request failed');
  }
  return response.json();
};

const api = {
  get: async (endpoint) => {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: 'GET',
      headers: getHeaders(),
    });
    return handleResponse(response);
  },
  post: async (endpoint, data, options = {}) => {
    const response = await fetch(`${BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: { ...getHeaders(), ...options.headers },
      body: data instanceof URLSearchParams ? data.toString() : JSON.stringify(data),
    });
    return handleResponse(response);
  },
};

export default api;
