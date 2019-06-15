import distributions
binom=distributions.Binomial()
binom.read_data_file('numbers_binomial.txt')
print(binom.pdf(3))
print(f'n is {binom.n} p is {binom.p} data is {binom.data}')