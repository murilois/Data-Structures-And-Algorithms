def fibonacci(n, memo=None):
    """
    Calcula o n-ésimo número da sequência de Fibonacci usando recursão com memoização.

    A memoização (cache) armazena resultados de chamadas anteriores para evitar
    cálculos repetidos, tornando a função muito mais rápida para valores maiores de n.

    Args:
        n (int): A posição na sequência (deve ser um inteiro não negativo).
        memo (dict, optional): Dicionário usado internamente para o cache.
                               Não precisa ser fornecido na chamada inicial.

    Returns:
        int: O número de Fibonacci na posição n.

    Raises:
        ValueError: Se 'n' não for um inteiro não negativo.
    """
    # Inicializa o dicionário de memoização na primeira chamada
    if memo is None:
        memo = {}

    # Validação da entrada
    if not isinstance(n, int) or n < 0:
        raise ValueError("A entrada deve ser um inteiro não negativo.")

    # 1. Verifica se o resultado já está no cache
    if n in memo:
        return memo[n]

    # 2. Casos base da recursão
    if n <= 1:
        return n

    # 3. Passo recursivo: calcula, armazena no cache e retorna
    resultado = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    memo[n] = resultado
    return resultado

## Teste