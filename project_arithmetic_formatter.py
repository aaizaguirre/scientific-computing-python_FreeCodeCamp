def arithmetic_arranger(problems, show_answers=False):
    
    # No deben haber más de 5 problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dash_line = []
    result_line = []

    for problem in problems:
        parts = problem.split()
        
        # Manejo de errores
        if len(parts) !=3:
            return "Error: Invalid problem format."    
        first, operator, second = parts
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calcular ancho necesario + 2 (operador y espacio)
        width = max(len(first), len(second)) + 2

        # Formatear cada parte alineada
        top = first.rjust(width)
        bottom = operator + ' ' + second.rjust(width - 2)
        line = "-" * width
        result = str(eval(problem)).rjust(width)

        # Agregar a los niveles correspondientes
        first_line.append(top)
        second_line.append(bottom)
        dash_line.append(line)

        if show_answers:
            result_line.append(result)

    # Unión
    arranged_problems = '    '.join(first_line) + '\n' + \
                        '    '.join(second_line) + '\n' + \
                        '    '.join(dash_line)

    if show_answers:
        arranged_problems += '\n' + '    '.join(result_line)  

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')