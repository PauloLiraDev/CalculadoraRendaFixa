import streamlit as st
from functions import get_selic_annual, calculate_investment, compost_interest, aliquot_ir

selic_annual = get_selic_annual()

# Título do aplicativo
st.markdown("<h1 style='text-align: center; color: green;'>Calculadora de Investimento em Renda Fixa</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>SELIC Anual: {selic_annual:.2f}%</h3>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>SELIC Mensal: {selic_annual / 12:.4f}%</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>(Dados atualizados em tempo real pelo Banco Central)</p>", unsafe_allow_html=True)

# Entrada do usuário para o valor do investimento
st.markdown("<h3>Insira os dados do investimento:</h3>", unsafe_allow_html=True)
amount = st.number_input("Valor do investimento", min_value=0.0)
months = st.number_input("Quantidade de meses", min_value=0, step=1)
cdi_percentage = st.number_input("Porcentagem do CDI (%)", min_value=0.0, max_value=300.0, value=100.0)

# Botão que calcula rentabilidade
if st.button("Calcular Rentabilidade"):
    monthly_return = calculate_investment(cdi_percentage, selic_annual)
    total = compost_interest(principal=amount, rate=monthly_return / 100, time=months)
    ir = aliquot_ir(months)
    tax = (total - amount) * ir / 100
    st.markdown(f"<h3>Resultados:</h3>", unsafe_allow_html=True)
    st.write(f"Rentabilidade total bruta: :green[{total - amount:.2f} BRL]")
    st.write(f"Imposto de Renda: :red[-{tax:.2f} BRL] (A alíquota será de {ir}% para {months} meses).")
    st.success(f"Rendimento líquido de {total - amount - tax:.2f} BRL")

# Rodapé
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'> Desenvolvido por Paulo Lira </p>", unsafe_allow_html=True)