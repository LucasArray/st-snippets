const getUser = async (id) => {
    const response = await fetch(
      `https://api.example.com/users/${id}`
    );
  
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }
  
    return response.json();
  };