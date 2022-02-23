const navBtn = document.getElementById('nav-btn');
const cancelBtn = document.getElementById('cancel');
const sideNav = document.getElementById('sidenav');
const modal = document.getElementById('modal');

navBtn.addEventListener("click", function(){
    sideNav.classList.add('show');
    modal.classList.add('showModal');
});

cancelBtn.addEventListener("click",function(){
    sideNav.classList.remove('show');
    modal.classList.remove('showModal');
});


