document.getElementById('humburger-menu-open').addEventListener('click', function() {
    const open = document.getElementById('humburger-menu-open');
    const close = document.getElementById('humburger-menu-close');
    const menu = document.getElementById('menu');

    open.style.display = 'none';
    close.style.display = 'flex';
    menu.style.display = 'block';
});

document.getElementById('humburger-menu-close').addEventListener('click', function() {
    const open = document.getElementById('humburger-menu-open');
    const close = document.getElementById('humburger-menu-close');
    const menu = document.getElementById('menu');

    open.style.display = 'flex';
    close.style.display = 'none';
    menu.style.display = 'none';
});

