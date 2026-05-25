// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
const mobileLinks = mobileMenu.querySelectorAll('a');
mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.remove('active');
    });
});

// Module Filter
const filterTabs = document.querySelectorAll('.filter-tab');
const moduleCards = document.querySelectorAll('.module-card');

filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove active class from all tabs
        filterTabs.forEach(t => t.classList.remove('active'));
        // Add active class to clicked tab
        tab.classList.add('active');

        const filterValue = tab.getAttribute('data-filter');

        // Filter cards
        moduleCards.forEach(card => {
            const cardCategory = card.getAttribute('data-category');
            if (filterValue === 'all' || cardCategory === filterValue) {
                card.style.display = 'block';
                setTimeout(() => {
                    card.style.opacity = '1';
                }, 10);
            } else {
                card.style.opacity = '0';
                setTimeout(() => {
                    card.style.display = 'none';
                }, 300);
            }
        });
    });
});

// Module Pricing Expansion
const moduleToggles = document.querySelectorAll('.module-toggle');

moduleToggles.forEach(toggle => {
    toggle.addEventListener('click', (e) => {
        // Don't trigger if clicking a button inside the pricing wrapper
        if (e.target.closest('button') && e.target.closest('.pricing-grid')) {
            return;
        }

        const moduleId = toggle.getAttribute('data-module');
        const pricingWrapper = toggle.querySelector(`[data-module-id="${moduleId}"]`);

        // Close all other open pricing wrappers
        document.querySelectorAll('.module-pricing-wrapper.open').forEach(wrapper => {
            if (wrapper !== pricingWrapper) {
                wrapper.classList.remove('open');
            }
        });

        // Toggle current pricing wrapper
        pricingWrapper.classList.toggle('open');
    });
});

// Form Submission
const enterpriseForm = document.getElementById('enterprise-form');
const successBanner = document.getElementById('success-banner');

enterpriseForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Simple validation
    const fullName = document.getElementById('full-name').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const email = document.getElementById('email').value.trim();
    const tenantCount = document.getElementById('tenant-count').value;
    const message = document.getElementById('message').value.trim();

    if (!fullName || !phone || !email || !tenantCount || !message) {
        alert('Please fill in all fields');
        return;
    }

    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email');
        return;
    }

    // Simulate form submission
    enterpriseForm.style.display = 'none';
    successBanner.classList.remove('hidden');

    // Optional: Reset form after a delay
    setTimeout(() => {
        enterpriseForm.reset();
        enterpriseForm.style.display = 'block';
        successBanner.classList.add('hidden');
    }, 5000);
});

// Smooth scroll for navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add animation classes on page load
window.addEventListener('load', () => {
    const fadeInElements = document.querySelectorAll('.fade-in-up');
    fadeInElements.forEach((el, index) => {
        el.style.animationDelay = `${index * 0.1}s`;
    });
});

// Intersection Observer for lazy animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all stat cards and module cards
document.querySelectorAll('.stat-card, .module-card, .tenant-box').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'all 0.6s ease forwards';
    observer.observe(el);
});