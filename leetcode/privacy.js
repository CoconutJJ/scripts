const originalEventListener = document.addEventListener;

document.addEventListener = function (type, listener, options) {


  
  if (type === "visibilitychange") return;

  originalEventListener(type, listener, options);
};
