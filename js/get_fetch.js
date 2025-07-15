const fetchUserData = async (userId) => {
    try {
      const response = await fetch(
        `https://api.example.com/users/${userId}`
      );
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Fetch failed:', error);
    }
  };