function loadConfigFile(path) {
  return fetch(path)
    .then(response => response.json());
}
  
Promise.all([loadConfigFile("../../data/config/scale_dict.json"),
             loadConfigFile("../../data/config/threshold_dict.json")
])
  .then(([scale_dict, threshold_dict]) => {
    const config = {
      scale_dict: scale_dict,
      threshold_dict: threshold_dict
    };

    const event = new CustomEvent('configLoading', {
      detail: config
    });

    document.dispatchEvent(event);
  })
  .catch(error => {
    console.error('Failed to load config:', error);
});