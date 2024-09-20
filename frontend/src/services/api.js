const API_URL = process.env.REACT_APP_API_URL;

export const fetchData = async () => {
  const response = await fetch(`${API_URL}/data`);
  return response.json();
};
