# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:22:23 2022

@author: Dell inspiron
"""

import streamlit as st
import pandas as pd

def main():
    clientes_df = pd.read_excel('Clientes.xlsx')
    
    produtos_df = pd.read_excel('Produtos.xlsx')
    
    
    transportadoras_df = pd.read_excel('Transportadoras.xlsx')
    
    st.header('Notas Fiscais - Indatex')
    st.markdown('---')
    
    st.subheader('Cliente')
    cliente = st.selectbox('Escolha o Cliente: ', clientes_df)
    razao_s = clientes_df[clientes_df['Nome']==cliente]['Razão Social'].iloc[0]
    cnpj = clientes_df[clientes_df['Nome']==cliente]['CNPJ'].iloc[0]
    st.markdown('---')
    
    st.subheader('Produtos')
    qtd_prod = st.number_input('Quantos Produtos diferentes :', min_value=0, max_value=10)
    
    produtos_list = []
    for i in range(1,qtd_prod+1):
    
        produto = st.selectbox('Escolha o Produto: ', produtos_df, key=i)
        produtos_list.append(produto)
    
    st.markdown('---')
    st.subheader('Quantidade e Preço')
    
    j=0
    k=100
    peso_sug=0
    
    produtos_total = []
    for prod in produtos_list:
        st.write(prod)
        qtd_prod = st.number_input('Quantidade :', key=j, format='%f')
        preco_unit = st.number_input('Preço unit. :', key=k, format='%f')
        
        peso_sug += qtd_prod*pd.DataFrame(produtos_df[produtos_df['Nome'] == prod]['Peso']).iloc[0,0]
        
        unid = pd.DataFrame(produtos_df[produtos_df['Nome'] == prod]['Unidade']).iloc[0,0]
        p_string = f'**{qtd_prod}** {unid} de **{prod}** a R\$ **{preco_unit}** / {unid} >>> Total de **R\$ {round(qtd_prod*preco_unit,2)}**'
        st.markdown(p_string)
        produtos_total.append(p_string)
        st.markdown('---')
        j += 1
        k -=1
        
    st.markdown('---')
    st.subheader('Transporte e Frete')
    
    transportadora = st.selectbox('Escolha a Transportadora', transportadoras_df)
    
    caixas = st.number_input('Quantas Caixas :', key=1025, min_value=1)
    
    peso = st.number_input('Peso Total (Sugerido):',min_value=peso_sug ,key=1026, format='%f')
    
    frete = st.selectbox('Frete :', ['Nosso', 'Dele'])
    
    st.markdown('---')
    st.subheader('Condições de Pagamento')
    
    pagamento = st.radio('Pagamento :', ['à vista', 'a prazo'])
    
    if pagamento=='a prazo':
        dates = []
        parcelas = st.number_input('Em quantas vezes :', min_value=1)
        
        for i in range(1,parcelas+1):
            date = st.date_input(f'Vencimento {i}')
            dates.append(date)
            
    ordem = st.number_input('Ordem de Compra: (Se não existe, coloque 0)', min_value=0)
            
    #m=1
    #for d in dates: 
    #    st.write(f'vencimento {m} : {d.strftime("%d/%m/%Y")}')
    #    m+=1
        
    st.markdown('---')    
    st.subheader('Enviar para o Escritório')
    
    st.write(f'**Cliente**: {razao_s}')
    st.write(f'**CNPJ**: {cnpj}')
    st.write(f'**Produtos**:')
    for p in produtos_total:
        st.write(p)
        
    st.write(f'**Transportadora**: {transportadora}')
    if frete == 'Dele':
        st.write(f'**Frete**: FOB')
    else:
        st.write(f'**Frete**: CIF')
    
    st.write(f'{caixas} Caixas >>>  {round(peso,0)} kg Líquido ou {round(peso+caixas ,0)} kg Bruto ')
    
    st.write(f'**Pagamento** : {pagamento}')
    
    m = 1
    if pagamento=='a prazo':
        for d in dates: 
            st.write(f'**vencimento {m}** : {d.strftime("%d/%m/%Y")}')
            m+=1
            
    if ordem == 0:
        st.write('**Ordem de Compra: ** Sem ordem')
    else:
        st.write(f'**Ordem de Compra: ** {ordem}')
        
main()

    