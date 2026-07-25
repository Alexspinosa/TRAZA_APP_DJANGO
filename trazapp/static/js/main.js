// Toggle de tema oscuro/claro
const themeBtn = document.getElementById('themeToggle');
const root = document.documentElement;
themeBtn?.addEventListener('click', () => {
    const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('trazapp-theme', next);
});
const savedTheme = localStorage.getItem('trazapp-theme');
if (savedTheme) root.setAttribute('data-theme', savedTheme);


// Secciones colapsables del sidebar
document.querySelectorAll('.nav-group').forEach((group) => {
    const groupName = group.dataset.group;
    const storageKey = `trazapp-nav-${groupName}`;
    const toggle = group.querySelector('.nav-group-toggle');
    const hasActiveItem = group.querySelector('.trace-item.is-active') !== null;

    // Decide si debe abrir: activo guardado > tiene el link activo > abierta por defecto
    const saved = localStorage.getItem(storageKey);
    const shouldOpen = saved !== null
        ? saved === 'open'
        : (hasActiveItem || group.dataset.defaultOpen === 'true');

    if (shouldOpen) group.classList.add('is-open');

    toggle?.addEventListener('click', () => {
        const isOpen = group.classList.toggle('is-open');
        localStorage.setItem(storageKey, isOpen ? 'open' : 'closed');
    });
});