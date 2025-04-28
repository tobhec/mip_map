fetch('colour_thresholds.json')
  .then(response => response.json())
  .then(colour_thresholds => {
    document.dispatchEvent(new CustomEvent("colourThresholdsReady", {detail: colour_thresholds}));
  })
  .catch(error => console.error('Error:', error));