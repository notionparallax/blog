async function makeRequest(method, url) {
  const response = await fetch(url, { method });
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return await response.text();
}
