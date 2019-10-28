document.querySelectorAll('[data-fallback-select]').forEach(div => {
    const realInput = div.querySelector('.real');
    const fallbackInput = div.querySelector('.fallback');
    const selectInput = div.querySelector('select');
    const fallbackValue = div.getAttribute("data-fallback-select");
    fallbackInput.addEventListener('change', (event) => {
      realInput.value = event.target.value;
    });
    selectInput.addEventListener('change', (event) => {
      const value = event.target.value;
      if (value === fallbackValue) {
          fallbackInput.style.display = "inline-block";
      } else {
          fallbackInput.style.display = "none";
          realInput.value = value;
      }
    });
});