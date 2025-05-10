fetch('../../data/output/scale_dict.json')
  .then(response => response.json())
  .then(colour_thresholds => {
    document.dispatchEvent(new CustomEvent("configLoading", {detail: colour_thresholds}));
    console.log("Step 1");
  })
  .catch(error => console.error('Error:', error));