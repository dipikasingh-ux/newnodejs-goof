const params = new URLSearchParams(window.location.search);
const user = params.get("user"");
const welcome = document.querySelector("Welcome")


welcome.innerHTML = 'welcome back, ${user}!';
console.log(user);
