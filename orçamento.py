projeto = input('Digite a descrição do projeto: ')
dias_estimados = input('Digite o total de dias estimados: ')
valor_dia = input('Digite valor do dia : ')

valor_total = int(dias_estimados) * int(valor_dia)
print(f'o valor total foi {valor_total}')

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial')
pdf.image('template.png', x=0 , y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, dias_estimados )
pdf.text(115, 175, valor_dia)
pdf.text(115, 190, str(valor_total))

pdf.output('Orçamento.pdf')
print('Orçamento gerado com sucesso! ')