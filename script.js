// Polynomial Calculator - Client Side
let calculationHistory = [];

// Parse polynomial string to coefficient array
function parsePolynomial(polyString) {
    const trimmed = polyString.trim().toLowerCase().replace(/\s+/g, '');
    
    if (!trimmed) {
        throw new Error('Empty polynomial string');
    }

    const coefficients = {};
    
    // Split by + and - while keeping the operators
    const terms = trimmed.match(/[+-]?[^+-]+/g) || [];
    
    terms.forEach(term => {
        term = term.trim();
        if (!term) return;

        let coeff = 1;
        let power = 0;

        if (term.includes('x')) {
            const parts = term.split('x');
            
            // Parse coefficient
            if (parts[0] === '' || parts[0] === '+') {
                coeff = 1;
            } else if (parts[0] === '-') {
                coeff = -1;
            } else {
                coeff = parseFloat(parts[0]);
            }

            // Parse power
            if (parts[1] === '') {
                power = 1;
            } else if (parts[1].startsWith('^')) {
                power = parseInt(parts[1].substring(1));
            }
        } else {
            coeff = parseFloat(term);
            power = 0;
        }

        if (coefficients[power]) {
            coefficients[power] += coeff;
        } else {
            coefficients[power] = coeff;
        }
    });

    return coefficients;
}

// Format polynomial for display
function formatPolynomial(coefficients) {
    const powers = Object.keys(coefficients)
        .map(Number)
        .sort((a, b) => b - a);

    if (powers.length === 0) return '0';

    return powers.map(power => {
        const coeff = coefficients[power];
        
        if (coeff === 0) return '';
        
        let term = '';
        
        if (power === 0) {
            term = Math.abs(coeff).toString();
        } else if (power === 1) {
            if (Math.abs(coeff) === 1) {
                term = 'x';
            } else {
                term = Math.abs(coeff) + 'x';
            }
        } else {
            if (Math.abs(coeff) === 1) {
                term = 'x^' + power;
            } else {
                term = Math.abs(coeff) + 'x^' + power;
            }
        }

        return (coeff > 0 && powers.indexOf(power) > 0 ? ' + ' : (coeff < 0 ? ' - ' : '')) + term;
    })
    .filter(t => t !== '')
    .join('')
    .replace(/^\s+/, '')
    .replace(/^\+\s+/, '');
}

// Display results
function displayResult(title, result, success = true) {
    const resultDisplay = document.getElementById('resultDisplay');
    const className = success ? 'result-success' : 'result-error';
    resultDisplay.innerHTML = `<span class="${className}">${title}:</span><br>${result}`;
    
    // Add to history
    const timestamp = new Date().toLocaleTimeString();
    calculationHistory.unshift({ title, result, timestamp });
    updateHistory();
}

// Update history display
function updateHistory() {
    const historyDisplay = document.getElementById('historyDisplay');
    
    if (calculationHistory.length === 0) {
        historyDisplay.innerHTML = '<p class="placeholder">No calculations yet...</p>';
        return;
    }

    historyDisplay.innerHTML = calculationHistory
        .slice(0, 10) // Show last 10
        .map(item => `<div class="history-item"><strong>${item.timestamp}</strong> - ${item.title}: ${item.result}</div>`)
        .join('');
}

// Clear history
function clearHistory() {
    calculationHistory = [];
    updateHistory();
    document.getElementById('resultDisplay').innerHTML = '<p class="placeholder">Results will appear here...</p>';
}

// Add polynomials
async function addPolynomials() {
    try {
        const poly1 = document.getElementById('poly1').value;
        const poly2 = document.getElementById('poly2').value;

        if (!poly1 || !poly2) {
            displayResult('Error', 'Please enter both polynomials', false);
            return;
        }

        const response = await fetch('/add_polynomials', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ poly1, poly2 })
        });

        const data = await response.json();
        
        if (data.error) {
            displayResult('Error', data.error, false);
        } else {
            displayResult('Sum', data.result);
        }
    } catch (error) {
        displayResult('Error', error.message, false);
    }
}

// Subtract polynomials
async function subtractPolynomials() {
    try {
        const poly1 = document.getElementById('poly1').value;
        const poly2 = document.getElementById('poly2').value;

        if (!poly1 || !poly2) {
            displayResult('Error', 'Please enter both polynomials', false);
            return;
        }

        const response = await fetch('/subtract_polynomials', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ poly1, poly2 })
        });

        const data = await response.json();
        
        if (data.error) {
            displayResult('Error', data.error, false);
        } else {
            displayResult('Difference', data.result);
        }
    } catch (error) {
        displayResult('Error', error.message, false);
    }
}

// Multiply polynomials
async function multiplyPolynomials() {
    try {
        const poly1 = document.getElementById('poly1').value;
        const poly2 = document.getElementById('poly2').value;

        if (!poly1 || !poly2) {
            displayResult('Error', 'Please enter both polynomials', false);
            return;
        }

        const response = await fetch('/multiply_polynomials', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ poly1, poly2 })
        });

        const data = await response.json();
        
        if (data.error) {
            displayResult('Error', data.error, false);
        } else {
            displayResult('Product', data.result);
        }
    } catch (error) {
        displayResult('Error', error.message, false);
    }
}

// Show evaluation input
function evaluatePolynomial() {
    const evalSection = document.getElementById('evalSection');
    if (evalSection.style.display === 'none') {
        evalSection.style.display = 'block';
    } else {
        evalSection.style.display = 'none';
    }
}

// Perform evaluation
async function performEvaluation() {
    try {
        const poly1 = document.getElementById('poly1').value;
        const xValue = parseFloat(document.getElementById('evalX').value);

        if (!poly1) {
            displayResult('Error', 'Please enter Polynomial 1', false);
            return;
        }

        if (isNaN(xValue)) {
            displayResult('Error', 'Please enter a valid x value', false);
            return;
        }

        const response = await fetch('/evaluate_polynomial', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ poly: poly1, x: xValue })
        });

        const data = await response.json();
        
        if (data.error) {
            displayResult('Error', data.error, false);
        } else {
            displayResult(`P(${xValue})`, data.result);
        }
    } catch (error) {
        displayResult('Error', error.message, false);
    }
}

// Display linked list structure
async function displayStructure() {
    try {
        const poly1 = document.getElementById('poly1').value;

        if (!poly1) {
            document.getElementById('resultDisplay').innerHTML = 
                '<span class="result-error">Error:</span> Please enter Polynomial 1';
            return;
        }

        const response = await fetch('/get_linked_list', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ poly: poly1 })
        });

        const data = await response.json();
        
        const visualSection = document.getElementById('visualSection');
        const linkedListDisplay = document.getElementById('linkedListDisplay');

        if (data.error) {
            linkedListDisplay.innerHTML = `<span class="result-error">Error:</span> ${data.error}`;
        } else {
            let html = '<div style="overflow-x: auto; display: flex; align-items: center;">';
            
            if (data.nodes && data.nodes.length > 0) {
                data.nodes.forEach((node, index) => {
                    html += `<div class="node-box">${node}</div>`;
                    if (index < data.nodes.length - 1) {
                        html += '<div class="arrow">→</div>';
                    }
                });
            }
            
            html += '<div class="arrow">→</div><span style="font-weight: bold;">NULL</span></div>';
            linkedListDisplay.innerHTML = html;
        }

        visualSection.style.display = 'block';
    } catch (error) {
        document.getElementById('resultDisplay').innerHTML = 
            `<span class="result-error">Error:</span> ${error.message}`;
    }
}

// Event listeners for Enter key
document.addEventListener('DOMContentLoaded', function() {
    const poly1Input = document.getElementById('poly1');
    const poly2Input = document.getElementById('poly2');
    const evalXInput = document.getElementById('evalX');

    if (poly1Input) {
        poly1Input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                poly2Input.focus();
            }
        });
    }

    if (poly2Input) {
        poly2Input.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                addPolynomials();
            }
        });
    }

    if (evalXInput) {
        evalXInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                performEvaluation();
            }
        });
    }
});
