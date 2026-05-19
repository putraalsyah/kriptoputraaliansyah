/* ── Theme ─────────────────────────────────────────────────── */
const html = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
const themeToggleMobile = document.getElementById('themeToggleMobile');
const themeIcon = document.getElementById('themeIcon');
const themeIconMobile = document.getElementById('themeIconMobile');
const themeLabel = document.getElementById('themeLabel');

let currentTheme = localStorage.getItem('theme') || 'dark';
applyTheme(currentTheme);

function applyTheme(theme) {
  html.setAttribute('data-theme', theme);
  currentTheme = theme;
  localStorage.setItem('theme', theme);
  const isDark = theme === 'dark';
  const iconClass = isDark ? 'fa-moon' : 'fa-sun';
  if (themeIcon) themeIcon.className = `fa-solid ${iconClass}`;
  if (themeIconMobile) themeIconMobile.className = `fa-solid ${iconClass}`;
  if (themeLabel) themeLabel.textContent = isDark ? 'Dark Mode' : 'Light Mode';
}

function toggleTheme() {
  applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
}

if (themeToggle) themeToggle.addEventListener('click', toggleTheme);
if (themeToggleMobile) themeToggleMobile.addEventListener('click', toggleTheme);

/* ── Sidebar ───────────────────────────────────────────────── */
const sidebar = document.getElementById('sidebar');
const menuToggle = document.getElementById('menuToggle');
const overlay = document.getElementById('overlay');

function openSidebar() {
  sidebar.classList.add('open');
  overlay.classList.add('show');
  document.body.style.overflow = 'hidden';
}
function closeSidebar() {
  sidebar.classList.remove('open');
  overlay.classList.remove('show');
  document.body.style.overflow = '';
}

if (menuToggle) menuToggle.addEventListener('click', openSidebar);
if (overlay) overlay.addEventListener('click', closeSidebar);

/* ── Copy to Clipboard ─────────────────────────────────────── */
function copyText(elementId, btn) {
  const el = document.getElementById(elementId);
  if (!el) return;
  navigator.clipboard.writeText(el.textContent.trim()).then(() => {
    const orig = btn.innerHTML;
    btn.innerHTML = '<i class="fa-solid fa-check"></i> Disalin!';
    btn.style.color = 'var(--success)';
    setTimeout(() => { btn.innerHTML = orig; btn.style.color = ''; }, 2000);
  });
}

/* ── Show/Hide helpers ─────────────────────────────────────── */
function showError(container, msg) {
  const el = container.querySelector('.error-box');
  if (!el) return;
  el.innerHTML = `<i class="fa-solid fa-circle-exclamation"></i> ${msg}`;
  el.classList.add('show');
}
function hideError(container) {
  const el = container.querySelector('.error-box');
  if (el) el.classList.remove('show');
}
function showLoading(container) {
  const el = container.querySelector('.loading');
  if (el) el.classList.add('show');
}
function hideLoading(container) {
  const el = container.querySelector('.loading');
  if (el) el.classList.remove('show');
}
function showResult(container) {
  const el = container.querySelector('.result-box');
  if (el) el.classList.add('show');
  const sc = container.querySelector('.steps-container');
  if (sc) sc.classList.add('show');
}

/* ── API helper ────────────────────────────────────────────── */
async function callApi(endpoint, payload) {
  const res = await fetch(endpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  return await res.json();
}

/* ── Mode tabs ─────────────────────────────────────────────── */
function initModeTabs(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const tabs = container.querySelectorAll('.mode-tab');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
    });
  });
}

/* ── Active mode getter ────────────────────────────────────── */
function getActiveMode(containerId) {
  const container = document.getElementById(containerId);
  if (!container) return 'encrypt';
  const active = container.querySelector('.mode-tab.active');
  return active ? active.dataset.mode : 'encrypt';
}

/* ── On load animation for rows ────────────────────────────── */
function animateRows(tableId) {
  const rows = document.querySelectorAll(`#${tableId} tbody tr`);
  rows.forEach((row, i) => {
    row.style.opacity = '0';
    row.style.transform = 'translateY(8px)';
    setTimeout(() => {
      row.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
      row.style.opacity = '1';
      row.style.transform = 'translateY(0)';
    }, i * 30);
  });
}
