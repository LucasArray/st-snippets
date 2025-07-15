const submitForm = (formElement) => {
    const formData = new FormData(formElement);
    fetch('/api/submit', {
      method: 'POST',
      body: formData,
    });
  };