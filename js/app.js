/* ================================================================
   TuneFry Dashboard — JavaScript
   Charts, animations, and interactions
   ================================================================ */

// ── Intersection Observer for scroll animations ────────────────
document.addEventListener('DOMContentLoaded', () => {
  // Animate elements on scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.observe-animate').forEach(el => observer.observe(el));

  // ── Velocity bar hover effects ──────────────────────────────
  document.querySelectorAll('.velocity-bar').forEach(bar => {
    bar.addEventListener('mouseenter', () => {
      if (!bar.classList.contains('hot')) {
        bar.style.background = 'rgba(255, 255, 255, 0.12)';
        bar.style.transform = 'scaleY(1.05)';
        bar.style.transformOrigin = 'bottom';
      }
    });
    bar.addEventListener('mouseleave', () => {
      if (!bar.classList.contains('hot')) {
        bar.style.background = '';
        bar.style.transform = '';
      }
    });
  });

  // ── Velocity dots carousel ──────────────────────────────────
  const dots = document.querySelectorAll('.velocity-dots .dot');
  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
      dots.forEach(d => d.classList.remove('active'));
      dot.classList.add('active');
    });
  });

  // ── Chart.js: Revenue Over Time (Stats page) ───────────────
  const revenueCtx = document.getElementById('revenueChart');
  if (revenueCtx && typeof Chart !== 'undefined') {
    const gradient = revenueCtx.getContext('2d');
    const grad = gradient.createLinearGradient(0, 0, 0, 280);
    grad.addColorStop(0, 'rgba(242, 101, 34, 0.3)');
    grad.addColorStop(1, 'rgba(242, 101, 34, 0)');

    new Chart(revenueCtx, {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
          label: 'Revenue ($)',
          data: [82, 96, 124, 148, 135, 162, 178, 195, 210, 219, 240, 258],
          borderColor: '#F26522',
          borderWidth: 2.5,
          backgroundColor: grad,
          fill: true,
          tension: 0.4,
          pointRadius: 0,
          pointHoverRadius: 6,
          pointHoverBackgroundColor: '#F26522',
          pointHoverBorderColor: '#fff',
          pointHoverBorderWidth: 2,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { intersect: false, mode: 'index' },
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: 'rgba(20, 20, 20, 0.95)',
            titleColor: '#8A8A8A',
            bodyColor: '#fff',
            bodyFont: { size: 14, weight: '700', family: 'Syne' },
            padding: 14,
            cornerRadius: 10,
            borderColor: 'rgba(255,255,255,0.1)',
            borderWidth: 1,
            callbacks: {
              label: (ctx) => `$${ctx.parsed.y.toFixed(2)}`
            }
          }
        },
        scales: {
          x: {
            grid: { color: 'rgba(255,255,255,0.04)', drawBorder: false },
            ticks: { color: '#555', font: { size: 11, family: 'Plus Jakarta Sans' } },
            border: { display: false }
          },
          y: {
            grid: { color: 'rgba(255,255,255,0.04)', drawBorder: false },
            ticks: {
              color: '#555',
              font: { size: 11, family: 'Plus Jakarta Sans' },
              callback: v => `$${v}`
            },
            border: { display: false }
          }
        }
      }
    });
  }

  // ── Chart.js: Streams Over Time (Stats page) ───────────────
  const streamsCtx = document.getElementById('streamsChart');
  if (streamsCtx && typeof Chart !== 'undefined') {
    const gradient2 = streamsCtx.getContext('2d');
    const grad2 = gradient2.createLinearGradient(0, 0, 0, 280);
    grad2.addColorStop(0, 'rgba(34, 197, 94, 0.2)');
    grad2.addColorStop(1, 'rgba(34, 197, 94, 0)');

    new Chart(streamsCtx, {
      type: 'bar',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
          label: 'Streams',
          data: [12400, 15800, 19200, 22100, 18900, 24500, 28700, 31200, 27800, 30100, 34500, 38200],
          backgroundColor: (ctx) => {
            const index = ctx.dataIndex;
            return index === ctx.chart.data.labels.length - 1 ? '#F26522' : 'rgba(255, 255, 255, 0.08)';
          },
          borderRadius: 8,
          borderSkipped: false,
          barPercentage: 0.6,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: 'rgba(20, 20, 20, 0.95)',
            titleColor: '#8A8A8A',
            bodyColor: '#fff',
            bodyFont: { size: 14, weight: '700', family: 'Syne' },
            padding: 14,
            cornerRadius: 10,
            borderColor: 'rgba(255,255,255,0.1)',
            borderWidth: 1,
            callbacks: {
              label: (ctx) => ctx.parsed.y.toLocaleString() + ' streams'
            }
          }
        },
        scales: {
          x: {
            grid: { display: false },
            ticks: { color: '#555', font: { size: 11, family: 'Plus Jakarta Sans' } },
            border: { display: false }
          },
          y: {
            grid: { color: 'rgba(255,255,255,0.04)', drawBorder: false },
            ticks: {
              color: '#555',
              font: { size: 11, family: 'Plus Jakarta Sans' },
              callback: v => v >= 1000 ? (v / 1000).toFixed(0) + 'k' : v
            },
            border: { display: false }
          }
        }
      }
    });
  }

  // ── Chart.js: Platform Breakdown Doughnut (Stats page) ─────
  const platformCtx = document.getElementById('platformChart');
  if (platformCtx && typeof Chart !== 'undefined') {
    new Chart(platformCtx, {
      type: 'doughnut',
      data: {
        labels: ['Spotify', 'Apple Music', 'YouTube Music', 'Amazon', 'Tidal', 'Other'],
        datasets: [{
          data: [42, 24, 15, 9, 6, 4],
          backgroundColor: [
            '#1DB954',
            '#FC3C44',
            '#FF0000',
            '#FF9900',
            '#00FFFF',
            'rgba(255,255,255,0.15)'
          ],
          borderWidth: 0,
          spacing: 3,
          borderRadius: 4,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '72%',
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: 'rgba(20, 20, 20, 0.95)',
            bodyColor: '#fff',
            bodyFont: { size: 13, weight: '600', family: 'Plus Jakarta Sans' },
            padding: 12,
            cornerRadius: 10,
            borderColor: 'rgba(255,255,255,0.1)',
            borderWidth: 1,
            callbacks: {
              label: (ctx) => `${ctx.label}: ${ctx.parsed}%`
            }
          }
        }
      }
    });
  }

  // ── Counter animation for stat values ──────────────────────
  const statValues = document.querySelectorAll('[data-count]');
  statValues.forEach(el => {
    const target = parseInt(el.dataset.count);
    const duration = 1500;
    const start = Date.now();

    function animate() {
      const elapsed = Date.now() - start;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 3);
      const current = Math.floor(ease * target);
      el.textContent = current.toLocaleString();
      if (progress < 1) requestAnimationFrame(animate);
    }
    animate();
  });

  // ── Search focus effect ─────────────────────────────────────
  const searchInput = document.querySelector('.search-box input');
  if (searchInput) {
    searchInput.addEventListener('focus', () => {
      searchInput.parentElement.style.transform = 'scale(1.02)';
      searchInput.parentElement.style.transition = 'transform 0.2s ease';
    });
    searchInput.addEventListener('blur', () => {
      searchInput.parentElement.style.transform = '';
    });
  }

  // ── Category tab switching + filtering (Marketplace page) ──
  const categoryTabs = document.querySelectorAll('.category-tab');
  if (categoryTabs.length) {
    categoryTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        categoryTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        const filter = tab.dataset.filter;
        const cards = document.querySelectorAll('.service-card[data-platform]');

        cards.forEach(card => {
          const match = filter === 'all' || card.dataset.platform === filter;
          card.style.display = match ? '' : 'none';
        });

        // Hide section headers if their grid has no visible cards
        document.querySelectorAll('.section-header').forEach(header => {
          const grid = header.nextElementSibling;
          if (grid && grid.classList.contains('service-grid')) {
            const anyVisible = [...grid.querySelectorAll('.service-card')].some(c => c.style.display !== 'none');
            header.style.display = anyVisible ? '' : 'none';
          }
        });
      });
    });
  }

  // ── Platform bar animation on load ─────────────────────────
  document.querySelectorAll('.platform-bar').forEach(bar => {
    const width = bar.style.width;
    bar.style.width = '0';
    setTimeout(() => {
      bar.style.width = width;
    }, 300);
  });

  // ── Connection toggle buttons ──────────────────────────────
  document.querySelectorAll('.conn-action').forEach(btn => {
    btn.addEventListener('click', () => {
      if (btn.classList.contains('connected-btn')) {
        btn.classList.remove('connected-btn');
        btn.textContent = 'Connect';
        const statusEl = btn.closest('.connection-card').querySelector('.conn-status');
        if (statusEl) {
          statusEl.textContent = 'Not connected';
          statusEl.classList.remove('connected');
        }
      } else {
        btn.classList.add('connected-btn');
        btn.textContent = 'Connected';
        const statusEl = btn.closest('.connection-card').querySelector('.conn-status');
        if (statusEl) {
          statusEl.textContent = 'Connected';
          statusEl.classList.add('connected');
        }
      }
    });
  });

  // ── Smooth page transitions ─────────────────────────────────
  document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', (e) => {
      const href = item.getAttribute('href');
      if (href && !href.startsWith('#')) {
        e.preventDefault();
        closeSidebar();
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.2s ease';
        setTimeout(() => {
          window.location.href = href;
        }, 200);
      }
    });
  });

  // ── Restore body opacity on load ────────────────────────────
  document.body.style.opacity = '1';
  document.body.style.transition = 'opacity 0.3s ease';

  // ── Close mobile sidebar on ESC ─────────────────────────────
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeSidebar();
  });

  // ── Tunefry Daily nav dropdown ───────────────────────────────
  // Auto-open if current page is ai-blog.html or daily.html context
  const page = window.location.pathname.split('/').pop();
  if (page === 'ai-blog.html' || page === 'daily.html') {
    const trigger = document.getElementById('dailyNavTrigger');
    const menu = document.getElementById('dailySubMenu');
    if (trigger && menu) {
      trigger.classList.add('open');
      menu.classList.add('open');
    }
  }
});

// ── Toggle Tunefry Daily sidebar dropdown ───────────────────────
function toggleDailyDropdown(el) {
  el.classList.toggle('open');
  const menu = document.getElementById('dailySubMenu');
  if (menu) menu.classList.toggle('open');
}

// ── Create Release topbar dropdown ──────────────────────────────
function toggleCreateDropdown(e) {
  e.stopPropagation();
  const dd = document.getElementById('createDropdown');
  if (!dd) return;
  dd.classList.toggle('open');
}
document.addEventListener('click', function() {
  const dd = document.getElementById('createDropdown');
  if (dd) dd.classList.remove('open');
});

// ── Mobile Sidebar Drawer ────────────────────────────────────────
function toggleSidebar() {
  const sidebar = document.querySelector('.sidebar');
  const overlay = document.getElementById('sidebarOverlay');
  if (!sidebar) return;
  const isOpen = sidebar.classList.toggle('open');
  if (overlay) overlay.classList.toggle('visible', isOpen);
  document.body.classList.toggle('sidebar-open', isOpen);
}

function closeSidebar() {
  const sidebar = document.querySelector('.sidebar');
  const overlay = document.getElementById('sidebarOverlay');
  if (!sidebar) return;
  sidebar.classList.remove('open');
  if (overlay) overlay.classList.remove('visible');
  document.body.classList.remove('sidebar-open');
}
