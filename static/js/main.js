const username = document.getElementById("username").getAttribute("data-username");

if (username) {
    localStorage.setItem("username", username);
    let user = localStorage.getItem("username");
    document.getElementById("username").textContent = user;
}
const logoutLink = document.getElementById("logout-link");
if (logoutLink) {
    logoutLink.addEventListener("click", function () {
        localStorage.removeItem("username");
    });
}