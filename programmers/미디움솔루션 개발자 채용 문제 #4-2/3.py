def polynomial_addition(exp1, exp2):
    # Create dictionaries to store the coefficients of each term in each expression
    coeffs1 = {}
    coeffs2 = {}

    # Split the expressions into individual terms
    terms1 = exp1.split(" + ")
    terms2 = exp2.split(" + ")

    # Parse the coefficients and exponents of each term in the first expression and store them in the coeffs1 dictionary
    for term in terms1:
        parts = term.split("x^")
        if len(parts) == 1:
            coeffs1[0] = int(parts[0])
        else:
            coeffs1[int(parts[1])] = int(parts[0])

    # Parse the coefficients and exponents of each term in the second expression and store them in the coeffs2 dictionary
    for term in terms2:
        parts = term.split("x^")
        if len(parts) == 1:
            coeffs2[0] = int(parts[0])
        else:
            coeffs2[int(parts[1])] = int(parts[0])

    # Combine the two dictionaries, adding coefficients for terms with the same exponent
    coeffs = {}
    for exp, coeff in coeffs1.items():
        if exp in coeffs2:
            coeffs[exp] = coeff + coeffs2[exp]
        else:
            coeffs[exp] = coeff
    for exp, coeff in coeffs2.items():
        if exp not in coeffs1:
            coeffs[exp] = coeff

    # Sort the dictionary by exponent in descending order
    sorted_coeffs = sorted(coeffs.items(), reverse=True)

    # Build the resulting expression by concatenating terms in the correct format
    result_terms = []
    for exp, coeff in sorted_coeffs:
        if coeff == 0:
            continue
        elif exp == 0:
            result_terms.append(str(coeff))
        # elif exp == 1:
        #     result_terms.append(f"{coeff}x")
        else:
            result_terms.append(f"{coeff}x^{exp}")
    result = " + ".join(result_terms)
    return result


exp1 = "2x^5 + 3x^3 + 2x^1"
exp2 = "6x^6 + 4x^4 + 3x^3 + 2x^2"
result = polynomial_addition(exp1, exp2)
print(result)
