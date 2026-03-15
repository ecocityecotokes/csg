import streamlit as st
import os
import folium
from streamlit_folium import st_folium

# Configuração
SECRET_KEY = os.environ.get('SECRET_KEY', 'ec-token-rs-2026')
PORT = int(os.environ.get('PORT', 8501))

# Configurar página
st.set_page_config(
    page_title="EC Token RS",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Session State
if 'user_tokens' not in st.session_state:
    st.session_state.user_tokens = 2847

# CSS
st.markdown("""
    <style>
    body, .main { background-color: #0b0f0e !important; color: #e8f5ee !important; }
    .stMetric { background-color: #141c17 !important; padding: 15px !important; border-radius: 10px !important; border: 1px solid #1e3325 !important; }
    .stButton > button { background-color: #1aff8c !important; color: #000 !important; font-weight: bold !important; border-radius: 8px !important; }
    h1, h2, h3 { color: #1aff8c !important; }
    [data-testid="stSidebar"] { background-color: #111815 !important; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 🌍 EC Token RS")
    st.markdown("**Cidade Sustentável Gamificada**")
    st.markdown("Porto Alegre, RS • 2026")
    st.divider()
    
    pagina = st.radio(
        "**Menu**",
        ["📊 Dashboard", "🗺️ Mapa", "👤 Meu Impacto", "🔔 Feed", "🛍️ Loja"],
        label_visibility="collapsed"
    )
    
    st.divider()
    st.markdown("### 👤 Você")
    st.markdown(f"**Tokens:** 🌿 {st.session_state.user_tokens}")
    st.markdown("**Nível:** 🌟 3")

# DASHBOARD
if "📊 Dashboard" in pagina:
    st.title("📊 Dashboard")
    st.markdown("Bem-vindo ao EC Token RS — sua jornada de impacto ambiental")
    st.divider()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🌿 Tokens", "2.847", "+320 semana")
    with col2:
        st.metric("♻️ Reciclagem", "42,3 kg", "+8.2 kg")
    with col3:
        st.metric("🌳 Árvores", "34", "+12 semana")
    with col4:
        st.metric("📚 Cursos", "8", "+1 novo")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Seu Impacto CO₂")
        st.metric("CO₂ Evitado", "172.8 kg", "38% meta")
        st.progress(0.38)
        st.caption("38% de 450 kg • 295 dias restantes")
    
    with col2:
        st.subheader("🏆 Ranking")
        st.metric("Posição", "#47 de 15.420", "🥈 Top 1%")
        st.info("💡 Faltam 234 tokens para top 30!")
    
    st.divider()
    st.subheader("🎯 Metas da Cidade")
    
    st.markdown("**🌳 Plantio de Árvores**")
    st.progress(0.847, "847 / 1.000 (84%)")
    
    st.markdown("**♻️ Reciclagem**")
    st.progress(0.724, "5.420 / 7.500 kg (72%)")
    
    st.markdown("**⚡ Energia**")
    st.progress(0.620, "1.240 / 2.000 kWh (62%)")

# MAPA
elif "🗺️ Mapa" in pagina:
    st.title("🗺️ Mapa de Ações")
    st.markdown("Veja ações sustentáveis em tempo real em Porto Alegre")
    st.divider()
    
    m = folium.Map(
        location=[-30.0277, -51.2287],
        zoom_start=13,
        tiles="OpenStreetMap"
    )
    
    folium.CircleMarker(
        location=[-30.0277, -51.2287],
        radius=10,
        popup="<b>Parque Farroupilha</b><br>12 árvores plantadas",
        color="#1aff8c",
        fill=True,
        fillColor="#1aff8c",
        weight=2,
        opacity=0.8
    ).add_to(m)
    
    folium.CircleMarker(
        location=[-30.0324, -51.2311],
        radius=10,
        popup="<b>Ponto Coleta Reciclável</b><br>425 kg coletados",
        color="#c084fc",
        fill=True,
        fillColor="#c084fc",
        weight=2,
        opacity=0.8
    ).add_to(m)
    
    folium.CircleMarker(
        location=[-30.0199, -51.2189],
        radius=10,
        popup="<b>Escola Sustentável</b><br>E.E. Simão Bolívia",
        color="#00cfff",
        fill=True,
        fillColor="#00cfff",
        weight=2,
        opacity=0.8
    ).add_to(m)
    
    st_folium(m, width=1400, height=600)

# MEU IMPACTO
elif "👤 Meu Impacto" in pagina:
    st.title("👤 Seu Perfil de Impacto")
    st.markdown("Histórico completo do seu envolvimento ambiental")
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🌿 Tokens", "2.847")
    with col2:
        st.metric("🌳 Árvores", "34")
    with col3:
        st.metric("♻️ Reciclagem", "42.3 kg")
    
    st.divider()
    
    st.subheader("📋 Informações")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Nome:** Sua Jornada Sustentável")
        st.markdown("**Localização:** Porto Alegre, RS")
    
    with col2:
        st.markdown("**Desde:** Agosto de 2024")
        st.markdown("**Nível:** 🌟 3")
    
    st.divider()
    
    if st.button("📥 Exportar Extrato PDF", use_container_width=True):
        st.success("✅ PDF gerado com sucesso!")

# FEED
elif "🔔 Feed" in pagina:
    st.title("🔔 Feed de Ações")
    st.markdown("Acompanhe as ações em tempo real da comunidade")
    st.divider()
    
    filtro = st.selectbox(
        "Filtrar:",
        ["Todos", "Ação", "Alerta", "Projeto", "Escola"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    feed_items = [
        {"usuario": "Marina V.", "acao": "reciclou 4,2 kg de plástico", "local": "Porto Alegre", "tokens": "+20 ♻️", "tempo": "2 min", "tag": "Reciclagem"},
        {"usuario": "E.E. Simão Bolívia", "acao": "bateu a meta mensal com 142 alunos", "local": "Porto Alegre", "tokens": "🏆 Meta", "tempo": "8 min", "tag": "Escola"},
        {"usuario": "João C.", "acao": "plantou 3 mudas de ipê", "local": "Parque Farroupilha", "tokens": "+150 🌿", "tempo": "22 min", "tag": "Plantio"},
        {"usuario": "Projeto", "acao": "Painéis Solares atingiu 68% de financiamento", "local": "Escola Farrapos", "tokens": "68% 🏗️", "tempo": "35 min", "tag": "Projeto"},
        {"usuario": "Ana S.", "acao": "reportou entulho crítico (28 confirmações)", "local": "Av. Assis Brasil", "tokens": "28 👍", "tempo": "41 min", "tag": "Alerta"}
    ]
    
    for item in feed_items:
        if filtro == "Todos" or filtro == item["tag"]:
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"**{item['usuario']}** {item['acao']}")
                    st.caption(f"📍 {item['local']} • 🏷️ {item['tag']} • há {item['tempo']}")
                with col2:
                    st.markdown(f"**{item['tokens']}**")
                st.divider()

# LOJA
elif "🛍️ Loja" in pagina:
    st.title("🛍️ Loja 24h Sustentável")
    st.markdown("Resgate seus tokens por produtos sustentáveis")
    st.divider()
    
    st.info(f"💰 **Saldo:** {st.session_state.user_tokens} 🌿")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🌱 Sementes")
        st.markdown("10 tipos diferentes")
        st.metric("Custo", "110 🌿")
        if st.button("Resgatar", key="btn_1", use_container_width=True):
            st.success("✅ Resgate realizado!")
    
    with col2:
        st.subheader("🧴 Sabonete Eco")
        st.markdown("100% biodegradável")
        st.metric("Custo", "80 🌿")
        if st.button("Resgatar", key="btn_2", use_container_width=True):
            st.success("✅ Resgate realizado!")
    
    with col3:
        st.subheader("🔋 Carregador Solar")
        st.markdown("Energia solar")
        st.metric("Custo", "450 🌿")
        if st.button("Resgatar", key="btn_3", use_container_width=True):
            st.success("✅ Resgate realizado!")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📚 Curso Online")
        st.markdown("Sustentabilidade urbana")
        st.metric("Custo", "200 🌿")
        if st.button("Resgatar", key="btn_4", use_container_width=True):
            st.success("✅ Resgate realizado!")
    
    with col2:
        st.subheader("🚀 Desconto Energia")
        st.markdown("R$ 10 na conta de luz")
        st.metric("Custo", "300 🌿")
        if st.button("Resgatar", key="btn_5", use_container_width=True):
            st.success("✅ Resgate realizado!")
    
    with col3:
        st.subheader("🎁 Kit Eco")
        st.markdown("Completo e pronto")
        st.metric("Custo", "250 🌿")
        if st.button("Resgatar", key="btn_6", use_container_width=True):
            st.success("✅ Resgate realizado!")

# FOOTER
st.divider()
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6b8c76;'>"
    "Desenvolvido com ❤️ para sustentabilidade | Porto Alegre, RS • 2026"
    "</div>",
    unsafe_allow_html=True
)
```

**Clique em:** `Commit new file`

---

# 📄 ARQUIVO 2: requirements.txt

**Clique em:** `Add file` → `Create new file`

**Nome do arquivo:** `requirements.txt`

**Cole exatamente isto:**
```
streamlit==1.28.0
folium==0.14.0
streamlit-folium==0.7.0
