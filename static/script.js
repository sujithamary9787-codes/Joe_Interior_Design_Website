document.addEventListener('DOMContentLoaded', () => {
    // 1. Service Data Array
    // Update the image filenames to match exactly what is in your static/images folder
    const services = [
        { 
            title: "Luxury Kitchen", 
            image: "file1.jpg" 
        },
        { 
            title: "Modern Living Room", 
            image: "file2.jpg" 
        },
        { 
            title: "Creative Study Room", 
            image: "file3.jpg" 
        },
        { 
            title: "Smart Wardrobe", 
            image: "file4.jpg" 
        },
        { 
            title: "Pooja Room", 
            image: "file5.jpg" 
        },
        { 
            title: "Pooja Room", 
            image: "file6.jpg" 
        }
        { 
            title: "Modern Bathroom", 
            image: "file7.jpg" 
        }
    ];

    const serviceGrid = document.getElementById('serviceGrid');

    // 2. Generate Service Cards Dynamically
    if (serviceGrid) {
        services.forEach(service => {
            const card = document.createElement('div');
            // Tailwind classes for styling the card
            card.className = "bg-white rounded-2xl overflow-hidden shadow-md flex flex-col items-center p-4 transition-transform hover:scale-105";
            
            card.innerHTML = `
                <div class="w-full h-64 overflow-hidden rounded-xl mb-4">
                    <img src="/static/images/${service.image}" alt="${service.title}" class="w-full h-full object-cover">
                </div>
                <h3 class="text-xl font-bold mb-3">${service.title}</h3>
                <a href="#home" class="service-btn">
                    Get Quote
                </a>
            `;
            serviceGrid.appendChild(card);
        });
    }

    // 3. Modal Logic (If you use the pop-up for specific inquiries)
    const modal = document.getElementById('quoteModal');
    
    window.openModal = function() {
        if(modal) modal.classList.remove('hidden');
    };

    window.closeModal = function() {
        if(modal) modal.classList.add('hidden');
    };

    // Close modal when clicking outside of the content box
    window.onclick = function(event) {
        if (event.target == modal) {
            closeModal();
        }
    };

    // 4. Smooth Scroll for Navigation Links
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId.startsWith('#')) {
                e.preventDefault();
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});