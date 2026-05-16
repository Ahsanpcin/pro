import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Pro Medical Assistant",
    page_icon="💊",
    layout="centered"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

.main-card {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #374151;
    margin-top: 10px;
    margin-bottom: 20px;
}

.med-name {
    font-size: 30px;
    font-weight: bold;
    color: #22c55e;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# MEDICINE DATABASE
# =====================================================

medicine_data = {

    "paracetamol": {
        "brand": "Panadol",
        "category": "Painkiller",
        "use": "Fever and pain relief",
        "dose": "500mg",
        "side_effects": "Nausea",
        "warning": "Avoid overdose",
        "prescription": "No",
        "storage": "Below 25°C",
        "rating": "4.8/5"
    },

    "ibuprofen": {
        "brand": "Brufen",
        "category": "NSAID",
        "use": "Pain and swelling",
        "dose": "400mg",
        "side_effects": "Stomach pain",
        "warning": "Take after food",
        "prescription": "No",
        "storage": "Cool place",
        "rating": "4.6/5"
    },

    "aspirin": {
        "brand": "Disprin",
        "category": "Blood Thinner",
        "use": "Pain and blood thinning",
        "dose": "75mg",
        "side_effects": "Bleeding",
        "warning": "Avoid in ulcers",
        "prescription": "No",
        "storage": "Dry place",
        "rating": "4.5/5"
    },

    "diclofenac": {
        "brand": "Voltaren",
        "category": "Painkiller",
        "use": "Joint pain",
        "dose": "50mg",
        "side_effects": "Acidity",
        "warning": "Avoid long use",
        "prescription": "No",
        "storage": "Room temperature",
        "rating": "4.4/5"
    },

    "tramadol": {
        "brand": "Tramal",
        "category": "Opioid",
        "use": "Severe pain",
        "dose": "50mg",
        "side_effects": "Sleepiness",
        "warning": "Can cause addiction",
        "prescription": "Yes",
        "storage": "Dry place",
        "rating": "4.3/5"
    },

    "amoxicillin": {
        "brand": "Amoxil",
        "category": "Antibiotic",
        "use": "Bacterial infection",
        "dose": "500mg",
        "side_effects": "Diarrhea",
        "warning": "Complete course",
        "prescription": "Yes",
        "storage": "Below 25°C",
        "rating": "4.7/5"
    },

    "azithromycin": {
        "brand": "Zithromax",
        "category": "Antibiotic",
        "use": "Chest infection",
        "dose": "500mg",
        "side_effects": "Nausea",
        "warning": "Avoid unnecessary use",
        "prescription": "Yes",
        "storage": "Cool place",
        "rating": "4.6/5"
    },

    "cefixime": {
        "brand": "Cefspan",
        "category": "Antibiotic",
        "use": "Typhoid and infections",
        "dose": "200mg",
        "side_effects": "Loose motion",
        "warning": "Doctor advice needed",
        "prescription": "Yes",
        "storage": "Dry place",
        "rating": "4.5/5"
    },

    "ciprofloxacin": {
        "brand": "Cipro",
        "category": "Antibiotic",
        "use": "Urine infection",
        "dose": "500mg",
        "side_effects": "Tendon pain",
        "warning": "Avoid gym",
        "prescription": "Yes",
        "storage": "Room temperature",
        "rating": "4.4/5"
    },

    "metronidazole": {
        "brand": "Flagyl",
        "category": "Antibiotic",
        "use": "Stomach infection",
        "dose": "400mg",
        "side_effects": "Metallic taste",
        "warning": "Avoid alcohol",
        "prescription": "Yes",
        "storage": "Cool place",
        "rating": "4.5/5"
    },

    "doxycycline": {
        "brand": "Doxy",
        "category": "Antibiotic",
        "use": "Skin infection",
        "dose": "100mg",
        "side_effects": "Sun sensitivity",
        "warning": "Avoid sunlight",
        "prescription": "Yes",
        "storage": "Dry place",
        "rating": "4.4/5"
    },

    "cetirizine": {
        "brand": "Zyrtec",
        "category": "Antihistamine",
        "use": "Allergy and itching",
        "dose": "10mg",
        "side_effects": "Sleepiness",
        "warning": "Avoid driving",
        "prescription": "No",
        "storage": "Room temperature",
        "rating": "4.4/5"
    },

    "loratadine": {
        "brand": "Claritin",
        "category": "Antihistamine",
        "use": "Sneezing and allergy",
        "dose": "10mg",
        "side_effects": "Headache",
        "warning": "Non drowsy",
        "prescription": "No",
        "storage": "Cool place",
        "rating": "4.3/5"
    },

    "fexofenadine": {
        "brand": "Allegra",
        "category": "Antihistamine",
        "use": "Seasonal allergy",
        "dose": "120mg",
        "side_effects": "Dizziness",
        "warning": "Take with water",
        "prescription": "No",
        "storage": "Dry place",
        "rating": "4.4/5"
    },

    "salbutamol": {
        "brand": "Ventolin",
        "category": "Asthma",
        "use": "Breathing problem",
        "dose": "2 puffs",
        "side_effects": "Fast heartbeat",
        "warning": "Do not overuse",
        "prescription": "Yes",
        "storage": "Avoid heat",
        "rating": "4.6/5"
    },

    "montelukast": {
        "brand": "Singulair",
        "category": "Asthma",
        "use": "Asthma and allergy",
        "dose": "10mg",
        "side_effects": "Headache",
        "warning": "Night dose preferred",
        "prescription": "Yes",
        "storage": "Cool place",
        "rating": "4.4/5"
    },

    "omeprazole": {
        "brand": "Losec",
        "category": "Acidity",
        "use": "Acidity and ulcer",
        "dose": "20mg",
        "side_effects": "Headache",
        "warning": "Before breakfast",
        "prescription": "No",
        "storage": "Dry place",
        "rating": "4.5/5"
    },

    "pantoprazole": {
        "brand": "Protonix",
        "category": "Acidity",
        "use": "GERD and acidity",
        "dose": "40mg",
        "side_effects": "Nausea",
        "warning": "Before food",
        "prescription": "No",
        "storage": "Room temperature",
        "rating": "4.5/5"
    },

    "ranitidine": {
        "brand": "Zantac",
        "category": "Acidity",
        "use": "Heartburn",
        "dose": "150mg",
        "side_effects": "Constipation",
        "warning": "Use carefully",
        "prescription": "No",
        "storage": "Cool place",
        "rating": "4.2/5"
    },

    "metformin": {
        "brand": "Glucophage",
        "category": "Diabetes",
        "use": "Type 2 diabetes",
        "dose": "500mg",
        "side_effects": "Weakness",
        "warning": "Take with meals",
        "prescription": "Yes",
        "storage": "Below 30°C",
        "rating": "4.7/5"
    },

    "insulin": {
        "brand": "Humulin",
        "category": "Diabetes",
        "use": "Control blood sugar",
        "dose": "Doctor prescribed",
        "side_effects": "Low sugar",
        "warning": "Monitor glucose",
        "prescription": "Yes",
        "storage": "Refrigerator",
        "rating": "4.8/5"
    },

    "glimepiride": {
        "brand": "Amaryl",
        "category": "Diabetes",
        "use": "Blood sugar control",
        "dose": "1mg",
        "side_effects": "Low sugar",
        "warning": "Do not skip meals",
        "prescription": "Yes",
        "storage": "Dry place",
        "rating": "4.5/5"
    },

    "amlodipine": {
        "brand": "Norvasc",
        "category": "Blood Pressure",
        "use": "High BP",
        "dose": "5mg",
        "side_effects": "Swelling",
        "warning": "Stand slowly",
        "prescription": "Yes",
        "storage": "Room temperature",
        "rating": "4.5/5"
    },

    "losartan": {
        "brand": "Cozaar",
        "category": "Blood Pressure",
        "use": "Hypertension",
        "dose": "50mg",
        "side_effects": "Dizziness",
        "warning": "Avoid in pregnancy",
        "prescription": "Yes",
        "storage": "Dry place",
        "rating": "4.4/5"
    },

    "atenolol": {
        "brand": "Tenormin",
        "category": "Blood Pressure",
        "use": "Heart rate control",
        "dose": "50mg",
        "side_effects": "Tiredness",
        "warning": "Do not stop suddenly",
        "prescription": "Yes",
        "storage": "Cool place",
        "rating": "4.4/5"
    },

    "atorvastatin": {
        "brand": "Lipitor",
        "category": "Cholesterol",
        "use": "Lower cholesterol",
        "dose": "10mg",
        "side_effects": "Muscle pain",
        "warning": "Avoid grapefruit",
        "prescription": "Yes",
        "storage": "Room temperature",
        "rating": "4.5/5"
    },

    "rosuvastatin": {
        "brand": "Crestor",
        "category": "Cholesterol",
        "use": "Lower bad cholesterol",
        "dose": "10mg",
        "side_effects": "Weakness",
        "warning": "Regular tests needed",
        "prescription": "Yes",
        "storage": "Dry place",
        "rating": "4.5/5"
    },

    "vitamin c": {
        "brand": "Ceevit",
        "category": "Vitamin",
        "use": "Boost immunity",
        "dose": "500mg",
        "side_effects": "Acidity",
        "warning": "Avoid excess use",
        "prescription": "No",
        "storage": "Cool place",
        "rating": "4.6/5"
    },

    "vitamin d": {
        "brand": "D Sun",
        "category": "Vitamin",
        "use": "Bone strength",
        "dose": "1000 IU",
        "side_effects": "Rare",
        "warning": "Avoid overdose",
        "prescription": "No",
        "storage": "Dry place",
        "rating": "4.5/5"
    },

    "calcium": {
        "brand": "Caltrate",
        "category": "Supplement",
        "use": "Bone health",
        "dose": "500mg",
        "side_effects": "Constipation",
        "warning": "Drink water",
        "prescription": "No",
        "storage": "Cool place",
        "rating": "4.4/5"
    },"augmentin": {
    "brand": "Augmentin",
    "category": "Antibiotic",
    "use": "Bacterial infections",
    "dose": "625mg",
    "side_effects": "Diarrhea",
    "warning": "Complete full course",
    "prescription": "Yes",
    "storage": "Cool place",
    "rating": "4.6/5"
},

"coamoxiclav": {
    "brand": "Co Amoxiclav",
    "category": "Antibiotic",
    "use": "Chest and throat infections",
    "dose": "625mg",
    "side_effects": "Nausea",
    "warning": "Take after food",
    "prescription": "Yes",
    "storage": "Dry place",
    "rating": "4.5/5"
},

"clarithromycin": {
    "brand": "Klacid",
    "category": "Antibiotic",
    "use": "Respiratory infections",
    "dose": "500mg",
    "side_effects": "Metallic taste",
    "warning": "Avoid overdose",
    "prescription": "Yes",
    "storage": "Room temperature",
    "rating": "4.5/5"
},

"levofloxacin": {
    "brand": "Levaquin",
    "category": "Antibiotic",
    "use": "Lung and urine infections",
    "dose": "500mg",
    "side_effects": "Dizziness",
    "warning": "Avoid heavy exercise",
    "prescription": "Yes",
    "storage": "Cool place",
    "rating": "4.4/5"
},

"moxifloxacin": {
    "brand": "Avelox",
    "category": "Antibiotic",
    "use": "Severe bacterial infections",
    "dose": "400mg",
    "side_effects": "Headache",
    "warning": "Use doctor advice",
    "prescription": "Yes",
    "storage": "Dry place",
    "rating": "4.4/5"
},

"fluconazole": {
    "brand": "Diflucan",
    "category": "Antifungal",
    "use": "Fungal infections",
    "dose": "150mg",
    "side_effects": "Stomach pain",
    "warning": "Avoid unnecessary use",
    "prescription": "Yes",
    "storage": "Room temperature",
    "rating": "4.5/5"
},

"ketoconazole": {
    "brand": "Nizoral",
    "category": "Antifungal",
    "use": "Skin fungal infection",
    "dose": "200mg",
    "side_effects": "Itching",
    "warning": "Avoid eye contact",
    "prescription": "No",
    "storage": "Cool place",
    "rating": "4.3/5"
},

"albendazole": {
    "brand": "Zentel",
    "category": "Anti Worm",
    "use": "Worm infections",
    "dose": "400mg",
    "side_effects": "Nausea",
    "warning": "Take after food",
    "prescription": "No",
    "storage": "Dry place",
    "rating": "4.4/5"
},

"mebendazole": {
    "brand": "Vermox",
    "category": "Anti Worm",
    "use": "Intestinal worms",
    "dose": "100mg",
    "side_effects": "Stomach cramps",
    "warning": "Avoid overdose",
    "prescription": "No",
    "storage": "Room temperature",
    "rating": "4.3/5"
},

"loperamide": {
    "brand": "Imodium",
    "category": "Diarrhea",
    "use": "Loose motion",
    "dose": "2mg",
    "side_effects": "Constipation",
    "warning": "Do not overuse",
    "prescription": "No",
    "storage": "Dry place",
    "rating": "4.5/5"
},

"ondansetron": {
    "brand": "Zofran",
    "category": "Anti Vomiting",
    "use": "Nausea and vomiting",
    "dose": "4mg",
    "side_effects": "Headache",
    "warning": "Use carefully",
    "prescription": "Yes",
    "storage": "Cool place",
    "rating": "4.6/5"
},

"domperidone": {
    "brand": "Motilium",
    "category": "Stomach",
    "use": "Vomiting and acidity",
    "dose": "10mg",
    "side_effects": "Dry mouth",
    "warning": "Before meals",
    "prescription": "Yes",
    "storage": "Room temperature",
    "rating": "4.4/5"
},

"dexamethasone": {
    "brand": "Decadron",
    "category": "Steroid",
    "use": "Inflammation and allergy",
    "dose": "0.5mg",
    "side_effects": "Weight gain",
    "warning": "Do not stop suddenly",
    "prescription": "Yes",
    "storage": "Dry place",
    "rating": "4.4/5"
},

"prednisolone": {
    "brand": "Predsol",
    "category": "Steroid",
    "use": "Severe allergy",
    "dose": "5mg",
    "side_effects": "Increased appetite",
    "warning": "Use doctor advice",
    "prescription": "Yes",
    "storage": "Cool place",
    "rating": "4.5/5"
},

"hydrocortisone": {
    "brand": "Cortaid",
    "category": "Steroid",
    "use": "Skin inflammation",
    "dose": "Cream",
    "side_effects": "Skin thinning",
    "warning": "External use only",
    "prescription": "No",
    "storage": "Room temperature",
    "rating": "4.3/5"
},

"diazepam": {
    "brand": "Valium",
    "category": "Anxiety",
    "use": "Anxiety and sleep issues",
    "dose": "5mg",
    "side_effects": "Sleepiness",
    "warning": "Can cause dependence",
    "prescription": "Yes",
    "storage": "Dry place",
    "rating": "4.4/5"
},

"alprazolam": {
    "brand": "Xanax",
    "category": "Anxiety",
    "use": "Panic and anxiety",
    "dose": "0.5mg",
    "side_effects": "Drowsiness",
    "warning": "Avoid alcohol",
    "prescription": "Yes",
    "storage": "Cool place",
    "rating": "4.5/5"
},

"sertraline": {
    "brand": "Zoloft",
    "category": "Depression",
    "use": "Depression and anxiety",
    "dose": "50mg",
    "side_effects": "Insomnia",
    "warning": "Do not stop suddenly",
    "prescription": "Yes",
    "storage": "Dry place",
    "rating": "4.5/5"
},

"warfarin": {
    "brand": "Coumadin",
    "category": "Blood Thinner",
    "use": "Prevent blood clots",
    "dose": "5mg",
    "side_effects": "Bleeding",
    "warning": "Regular blood test needed",
    "prescription": "Yes",
    "storage": "Room temperature",
    "rating": "4.4/5"
},

"clopidogrel": {
    "brand": "Plavix",
    "category": "Blood Thinner",
    "use": "Prevent heart attack",
    "dose": "75mg",
    "side_effects": "Bruising",
    "warning": "Avoid injury",
    "prescription": "Yes",
    "storage": "Cool place",
    "rating": "4.5/5"
},
}

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("💊 Medical Store Assistant")
st.sidebar.write("Developed by Ahsan 💊")

menu = st.sidebar.radio(
    "Select Page",
    [
        "Search Medicine",
        "All Medicines",
        "Statistics",
        "About"
    ]
)

# =====================================================
# MAIN TITLE
# =====================================================

st.title("💊 Pro Medical Assistant")

# =====================================================
# SEARCH PAGE
# =====================================================

if menu == "Search Medicine":

    medicine_names = sorted(list(medicine_data.keys()))

    search = st.selectbox(
        "Search Medicine",
        medicine_names
    )

    st.caption(
        "💡 Popular: paracetamol • ibuprofen • amoxicillin • cetirizine • omeprazole"
    )

    if search:

        info = medicine_data[search]

        st.markdown(f"""
        <div class="main-card">
            <p class="med-name">{search.title()}</p>
        </div>
        """, unsafe_allow_html=True)

        st.success(f"🏷 Brand: {info['brand']}")
        st.info(f"💊 Category: {info['category']}")
        st.warning(f"📌 Used For: {info['use']}")

        st.write(f"💉 Dose: {info['dose']}")
        st.write(f"⚠ Side Effects: {info['side_effects']}")
        st.write(f"🚫 Warning: {info['warning']}")
        st.write(f"📄 Prescription Required: {info['prescription']}")
        st.write(f"🧊 Storage: {info['storage']}")
        st.write(f"⭐ Rating: {info['rating']}")

# =====================================================
# ALL MEDICINES
# =====================================================

elif menu == "All Medicines":

    st.subheader("📋 Medicine Database")

    df = pd.DataFrame({
        "Medicine": [x.title() for x in medicine_data.keys()],
        "Category": [medicine_data[x]["category"] for x in medicine_data.keys()]
    })

    st.dataframe(df, use_container_width=True)

# =====================================================
# STATISTICS
# =====================================================

elif menu == "Statistics":

    st.subheader("📊 Statistics")

    total = len(medicine_data)

    prescription_yes = sum(
        1 for med in medicine_data.values()
        if med["prescription"] == "Yes"
    )

    prescription_no = total - prescription_yes

    col1, col2, col3 = st.columns(3)

    col1.metric("Total", total)
    col2.metric("Prescription", prescription_yes)
    col3.metric("Non Prescription", prescription_no)

    categories = {}

    for med in medicine_data.values():
        cat = med["category"]
        categories[cat] = categories.get(cat, 0) + 1

    chart_df = pd.DataFrame({
        "Category": list(categories.keys()),
        "Count": list(categories.values())
    })

    st.dataframe(chart_df, use_container_width=True)

# =====================================================
# ABOUT
# =====================================================

elif menu == "About":

    st.subheader("ℹ About")

    st.write("""
    ✅ Professional UI
    ✅ Mobile Friendly
    ✅ Fast Search
    ✅ Medical Store System
    ✅ Large Medicine Database
    ✅ Statistics System
    ✅ Clean Design
    """)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">
Made with Streamlit 💊
</div>
""", unsafe_allow_html=True)
