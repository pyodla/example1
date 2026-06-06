import streamlit as st
st.title("Exercise")

tab1, tab2, tab3, tab4 = st.tabs(["1. อายุงานที่เหลือ", "2. คำนวณหาค่า BMI", "3. ความดันโลหิต", "4. คัดกรองผู้ป่วย"])

with tab1:
    st.header("อายุงานที่เหลือ")
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("กรุณาใส่ชื่อ:")
    with col2:
        lname = st.text_input("กรุณาใส่นามสกุล:")
        
    col3, col4 = st.columns([1, 3])
    with col3:
        # ปรับค่าเริ่มต้น (value) เป็นอายุเฉลี่ยวัยทำงาน เช่น 30 จะได้ไม่เริ่มที่ 0 ปี
        user_age = st.number_input("กรุณาใส่อายุ:", min_value=0, max_value=120, value=30, step=1)
    with col4:
        user_career = st.text_input("กรุณาใส่อาชีพ:")

    # เพิ่มปุ่มกด เพื่อความสวยงามและเช็กความพร้อมของข้อมูล
    if st.button("คำนวณอายุงาน"):
        # เช็กว่ากรอกชื่อและนามสกุลหรือยัง
        if fname and lname: 
            if user_age < 60:
                retire = 60 - user_age
                st.success(f"ผู้ใช้งานชื่อคุณ **{fname} {lname}** อายุ {user_age} ปี ประกอบอาชีพ {user_career} "
                           f"เหลือเวลาทำงานอีก **{retire}** ปี ก่อนที่จะเกษียณอายุ (60 ปี)")
            else:
                st.info(f"คุณ **{fname} {lname}** อายุ {user_age} ปี ปัจจุบันถึงวัยเกษียณอายุการทำงานแล้ว ขอให้มีความสุขกับวัยเกษียณครับ! 🎉")
        else:
            st.warning("กรุณากรอกข้อมูล ชื่อ และ นามสกุล ให้ครบถ้วนก่อนคำนวณครับ")
    
with tab2:
    st.header("คำนวณค่า BMI")
    col5, col6 = st.columns(2)
    with col5:
        user_w = st.number_input("กรุณาน้ำหนัก(กิโลกรัม):", min_value=0.0, max_value=300.0, value=50.0, step=0.1)
    with col6:
        user_h = st.number_input("กรุณาใส่ส่วนสูง(เซนติเมตร):", min_value=0.0, max_value=250.0, value=160.0, step=0.1)
    if st.button("คำนวณค่า BMI"):
        height_m = user_h / 100
            # คำนวณ BMI
        bmi = user_w / (height_m ** 2)
        # แสดงผลลัพธ์ BMI (แสดงทศนิยม 2 ตำแหน่งด้วย :.2f)
        st.write(f"### ค่า BMI ของคุณคือ **{bmi:.2f}**")
        # แปลผลตามเกณฑ์สาธารณสุข
        if bmi < 18.5:
            st.warning("⚠️ **น้ำหนักน้อยกว่าเกณฑ์ (ผอม):** 🚨ควรทานอาหารที่มีประโยชน์และเพิ่มกล้ามเนื้อนะ!")
        elif 18.5 <= bmi < 24.99:
            st.success("⭐ **น้ำหนักสมส่วน (ปกติ):** ✨สุขภาพดีเยี่ยม รักษาระดับนี้ไว้ต่อไปนะ!")
        elif 25.0 <= bmi < 29.99:
            st.info("🟢 **น้ำหนักเกิน (ท้วม):** 😓เริ่มมีน้ำหนักเกินเล็กน้อย ลองควบคุมอาหารหวานมันดู!")
        elif 30.0 <= bmi < 34.99:
            st.warning("🟡 **อ้วน (ระดับ 1):** 😬เริ่มมีความเสี่ยงต่อสุขภาพ ควรออกกำลังกายสม่ำเสมอ")
        elif 35.0 <= bmi < 39.99:
            st.error("🟠 **อ้วนมาก (ระดับ 2):** 😨เสี่ยงต่อโรคแทรกซ้อนสูง แนะนำให้ปรึกษาผู้เชี่ยวชาญหรือแพทย์")
        else:
            st.error("🔴 **อ้วนมาก (ระดับ 3):** 😱เสี่ยงต่อโรคแทรกซ้อนอย่างมาก รีบปรึกษาแพทย์โดยด่วน!!!")

with tab3:
    st.header("ความดันโลหิตและการวิเคราะห์สุขภาพ")
    st.subheader("กรุณาใส่ค่าความดันโลหิต")
    col7, col8 = st.columns(2)
    with col7:
        sys_bp = st.number_input("ค่าความดันตัวบน (SYS - mmHg):", min_value=0, max_value=500, value=120, step=1)
    with col8:
        dia_bp = st.number_input("ค่าความดันตัวล่าง (DIA - mmHg):", min_value=0, max_value=250, value=80, step=1)

    if st.button("วิเคราะห์ผลความดันโลหิต"):
        st.write(f"### ผลตรวจความดันของคุณคือ **{sys_bp} / {dia_bp} mmHg**")

        if sys_bp >= 180 or dia_bp >= 110:
            st.error("🚨 **อันตราย! ความดันโลหิตสูง (ระดับ 3):** ค่าสูงเกินเกณฑ์มาก รีบแพทย์ทันที!!!")
            
        elif 160 <= sys_bp <= 179 or 100 <= dia_bp <= 109:
            st.error(" 😱**สูงมาก (ระดับ 2):** ค่าสูงเกินเกณฑ์มาก นั่งพักผ่อนแล้วลองวัดใหม่ หากยังสูงอยู่ควรปรึกษาแพทย์ทันทีนะ")
            
        elif 140 <= sys_bp <= 159 or 90 <= dia_bp <= 99:
            st.warning("😰 **สูง :** เริ่มน่ากังวลแล้วนะ ลองปรับพฤติกรรม ลดเค็ม ลดเครียด และคอยตรวจวัดบ่อยๆ")

        elif 130 <= sys_bp <= 139 or 85 <= dia_bp <= 89:
            st.warning("😰 **ค่อนข้างสูง (แต่ยังไม่เป็นโรค):** เริ่มเตือนภัยแล้วนะจ๊ะ อยู่ในระดับเฝ้าระวังจ้า")

        elif sys_bp < 90 or dia_bp < 60:
            st.info("📉 **ความดันโลหิตต่ำ:** หากมีอาการหน้ามืด วิงเวียนศีรษะ บ่อยๆ แนะนำให้ปรึกษาแพทย์เพิ่มเติมนะ")
            
        else:
            st.success("👍 **ปกติสมบูรณ์ดีเยี่ยม!** ความดันอยู่ในเกณฑ์สุขภาพดี ดูแลตัวเองแบบนี้ต่อไปนะคราบบบ 💯")

with tab4:
    st.header("การคัดกรองผู้ป่วย") 
    
    col9, col10 = st.columns(2)
    with col9:
        heart_rate = st.number_input("อัตราการเต้นของหัวใจ (ครั้ง/นาที):", min_value=0, max_value=300, value=75, step=1)
    with col10:
        SpO2 = st.number_input("ระดับออกซิเจนในเลือด (%):", min_value=0, max_value=100, value=98, step=1)
    col11, col12 = st.columns(2)
    with col11:
        blood_pressure = st.text_input("ความดันโลหิต (เช่น 120/80):", value="120/80")
    with col12:
        body_temp = st.number_input("อุณหภูมิร่างกาย (°C):", min_value=0.0, max_value=50.0, value=36.5, step=0.1)
    
    # [แก้ไข]: จัดย่อหน้าให้อยู่ในระดับหลักของ tab4 ไม่เยื้องไปอยู่ใน col12
    st.subheader("🧠 แบบประเมินความรู้สึกตัว (Glasgow Coma Scale: GCS)")
    
    # ใช้ st.expander เพื่อซ่อน/แสดง แบบประเมิน GCS
    with st.expander("คลิกเพื่อเปิดแบบประเมิน GCS (คะแนนเต็ม 15 คะแนน)"):
        
        # 1. การลืมตา (Eye Opening: E)
        gcs_e = st.radio(
            "1. การลืมตา (Eye Opening - E)",
            options=[
                (4, "4 คะแนน: ลืมตาได้เอง (Spontaneous)"),
                (3, "3 คะแนน: ลืมตาเมื่อเรียก (To speech)"),
                (2, "2 คะแนน: ลืมตาเมื่อเจ็บ (To pain)"),
                (1, "1 คะแนน: ไม่ลืมตาเลย (No response)")
            ],
            format_func=lambda x: x[1]
        )
        
        # 2. การตอบสนองทางวาจา (Verbal Response: V)
        gcs_v = st.radio(
            "2. การตอบสนองทางวาจา (Verbal Response - V)",
            options=[
                (5, "5 คะแนน: พูดคุยได้ปกติ ไม่สับสน (Oriented)"),
                (4, "4 คะแนน: พูดคุยได้แต่สับสน (Confused)"),
                (3, "3 คะแนน: พูดเป็นคำๆ ไม่มีประเด็น (Inappropriate words)"),
                (2, "2 คะแนน: ส่งเสียงไม่เป็นคำ/คราง (Incomprehensible sounds)"),
                (1, "1 คะแนน: ไม่ส่งเสียงเลย (No response)")
            ],
            format_func=lambda x: x[1]
        )
        
        # 3. การตอบสนองทางการเคลื่อนไหว (Motor Response: M)
        gcs_m = st.radio(
            "3. การตอบสนองทางการเคลื่อนไหว (Motor Response - M)",
            options=[
                (6, "6 คะแนน: ทำตามคำสั่งได้ถูกต้อง (Obeys commands)"),
                (5, "5 คะแนน: ทราบตำแหน่งที่เจ็บและพยายามปัดออก (Localizes pain)"),
                (4, "4 คะแนน: ชักแขนขาหนีเมื่อเจ็บ (Withdrawal จากความเจ็บปวด)"),
                (3, "3 คะแนน: แขนงอเข้าหาลำตัวเมื่อเจ็บ (Abnormal flexion / Decorticate)"),
                (2, "2 คะแนน: แขนเหยียดบิดออกเมื่อเจ็บ (Abnormal extension / Decerebrate)"),
                (1, "1 คะแนน: ไม่เคลื่อนไหวเลย (No response)")
            ],
            format_func=lambda x: x[1]
        )
        
        # รวมคะแนน GCS
        total_gcs = gcs_e[0] + gcs_v[0] + gcs_m[0]
        
        # แปลผลระดับความรุนแรงในกล่อง expander ทันที
        if 13 <= total_gcs <= 15:
            gcs_status = "🟢 ระดับเล็กน้อย (Mild Brain Injury) ผู้ป่วยรู้สึกตัวดี"
            st.success(f"**คะแนน GCS รวม: {total_gcs} คะแนน** ({gcs_status})")
        elif 9 <= total_gcs <= 12:
            gcs_status = "⚠️ ระดับปานกลาง (Moderate Brain Injury) มีภาวะซึม"
            st.warning(f"**คะแนน GCS รวม: {total_gcs} คะแนน** ({gcs_status})")
        else:
            gcs_status = "🚨 ระดับรุนแรงมาก/หมดสติ (Severe Brain Injury / Coma)"
            st.error(f"**คะแนน GCS รวม: {total_gcs} คะแนน** ({gcs_status})")

    # [แก้ไข]: ย้ายปุ่มออกมาอยู่ข้างนอกสุดของ tab4 และดันชุดโค้ดคำนวณทั้งหมดเยื้องเข้าไปอยู่ใต้ if สั่งงานของปุ่มนี้
    if st.button("เริ่มการคัดกรองผู้ป่วย"):
        # 🔒 ตรวจสอบรูปแบบความดันโลหิต
        if "/" in blood_pressure:
            try:
                sbp, dbp = blood_pressure.split("/")
                sbp = int(sbp.strip()) 
                dbp = int(dbp.strip())
                
                st.write("### 📋 ผลการคัดกรองเบื้องต้น")
                
                # ตรรกะคัดกรองสัญญาณชีพ (รวมการประเมิน GCS ร่วมด้วยเพื่อความสมบูรณ์แบบ)
                if SpO2 < 95 or body_temp >= 38.5 or sbp >= 160 or total_gcs <= 8:
                    st.error("🚨 **ผู้ป่วยเคสฉุกเฉินวิกฤต (สีแดง/เหลือง):** สัญญาณชีพผิดปกติ หรือคะแนนความรู้สึกตัว (GCS) ต่ำหมดสติ แนะนำส่งพบแพทย์ด่วนที่สุด! 😱")
                elif 37.5 <= body_temp < 38.5 or 130 <= sbp < 160 or 9 <= total_gcs <= 12:
                    st.warning("⚠️ **ผู้ป่วยสีเหลือง/เขียว (เฝ้าระวัง):** มีไข้ต่ำ ความดันเริ่มสูง หรือมีภาวะซึมเล็กน้อย ควรให้การรักษาเบื้องต้นและเฝ้าสังเกตอาการใกล้ชิด 😰")
                else:
                    st.success("👍 **สัญญาณชีพและระดับความรู้สึกตัวปกติ (สีขาว):** ผู้ป่วยอาการคงที่ ปลอดภัยดีคราบบบ 💯")
                    
            except ValueError:
                st.error("❌ **รูปแบบความดันไม่ถูกต้อง:** กรุณากรอกในรูปแบบ ตัวบน/ตัวล่าง เช่น 120/80 เท่านั้นครับ")
        else:
            st.warning("⚠️ กรุณากรอกค่าความดันโลหิตโดยใช้เครื่องหมาย / คั่นด้วยครับ เช่น 120/80")