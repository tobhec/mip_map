function loadConfigFile(path) {
  return fetch(path)
    .then(response => response.json());
}
  
Promise.all([loadConfigFile("../../data/output/scale_dict.json")])
  .then(([scale_dict]) => {
    const config = {
      scale_dict: scale_dict
    };

    const event = new CustomEvent('configLoading', {
      detail: config
    });

    document.dispatchEvent(event);
  })
  .catch(error => {
    console.error('Failed to load config:', error);
});