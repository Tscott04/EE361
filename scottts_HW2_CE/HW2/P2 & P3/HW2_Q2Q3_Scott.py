def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

def generate_prime_multiples_list(start, end):
    primes = prime_numbers_in_range(start, end)
    return [[p] + [p * i for i in range(2, 11)] for p in primes]

def apply_convolution(matrix, kernel):
    convolve_vals = []
    for sublist in matrix:
        first_five = sublist[:5]
        last_five = sublist[-5:]
        convolved_first = sum(first_five[i] * kernel[i] for i in range(len(kernel)))
        convolved_last = sum(last_five[i] * kernel[i] for i in range(len(kernel)))
        convolve_vals.append(convolved_first)
        convolve_vals.append(convolved_last)
    return convolve_vals

# Generate the list
result = generate_prime_multiples_list(2, 97)
print(result)

# Define the kernel
KERNEL = [-2, -1, 0, 1, 2]

# Apply convolution
convolve_vals = apply_convolution(result, KERNEL)

# Categorize based on threshold
threshold = 500
high_intensity = [val for val in convolve_vals if val >= threshold]
low_intensity = [val for val in convolve_vals if val < threshold]

# Print results
print("Convolve Values Length:", len(convolve_vals))
print("Convolve Values:", convolve_vals)
print("High Intensity Length:", len(high_intensity))
print("High Intensity:", high_intensity)
print("Low Intensity Length:", len(low_intensity))
print("Low Intensity:", low_intensity)