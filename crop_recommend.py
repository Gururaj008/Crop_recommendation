import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
from streamlit_option_menu import option_menu

def predict(listn):
    #st.markdown(listn)
    with open('crop_suggestion.pkl','rb') as file:
        model = pickle.load(file)
        return model.predict(listn)


if __name__=="__main__":
    st.set_page_config(layout="wide")
    col101, col102, col103 = st.columns([50,200,50])
    with col102:
           st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text { font-family: 'Agdasima', sans-serif; font-size: 70px;color:cyan }
                    </style>
                    <p class="custom-text"> Crop recommendation engine</p>
                    """, unsafe_allow_html=True)
    st.write('')
    st.write('')
    selected = option_menu(None, ["About the project","Crop recommendation","Developer contact details"], 
    icons=['pencil-square', 'male-farmer',  'file-person-fill'], menu_icon="cast", default_index=0, orientation="horizontal")
    st.write('')
    st.write('')
    if selected == 'About the project':
        st.markdown('<div style="text-align: justify"> Farmers play a pivotal role in India, where agriculture has been the backbone of the nation\'s economy and culture for centuries. Their significance cannot be overstated, as they are the primary source of food production for a vast and diverse population. India\'s agrarian sector not only provides sustenance but also contributes significantly to the country\'s GDP and employment. Farmers are custodians of the land, responsible for its fertility and sustainability. They embrace traditional wisdom while also adopting modern agricultural practices, striving to meet the growing demands of a burgeoning population. Their resilience in the face of various challenges, including adverse weather conditions and market fluctuations, is commendable. Moreover, they are the custodians of India\'s rich biodiversity, preserving countless indigenous crops and varieties. The importance of farmers in India extends beyond economic contributions, encompassing social and cultural dimensions, making them the backbone of the nation\'s identity and progress. Recognizing and supporting their efforts is crucial for ensuring food security, economic stability, and the overall well-being of the country.   </div>', unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.markdown('<div style="text-align: justify"> Artificial Intelligence (AI) holds immense potential to revolutionize agriculture and significantly benefit farmers. Through AI-powered technologies, farmers can access valuable insights and data-driven solutions that enhance crop management, optimize resource allocation, and improve overall productivity. AI can analyze vast amounts of data, including weather patterns, soil quality, and crop health, to provide precise recommendations on when to plant, irrigate, and harvest. Machine learning models can predict disease outbreaks and pest infestations, enabling early intervention and reducing crop losses. Moreover, AI-driven automation can streamline tasks such as harvesting and sorting, reducing labor costs and ensuring efficiency. AI-powered drones and sensors can monitor fields in real-time, helping farmers make informed decisions promptly. In essence, AI empowers farmers with the tools and knowledge needed to make agriculture more sustainable, efficient, and resilient in the face of the evolving challenges of modern farming.   </div>', unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.markdown('<div style="text-align: justify"> Recommending crop choices for farmers based on soil and weather conditions is of paramount importance in modern agriculture. These recommendations not only optimize crop yield and quality but also contribute significantly to sustainable and efficient farming practices. Soil quality and composition can vary widely even within a single region, and selecting the right crop that matches the soil\'s characteristics ensures optimal growth and reduces the need for excessive fertilizers or chemicals. Weather conditions, including rainfall patterns and temperature fluctuations, play a crucial role in determining crop success. Providing farmers with accurate and timely recommendations based on these factors helps mitigate risks associated with adverse weather events and climate change. Ultimately, tailoring crop choices to local soil and weather conditions not only boosts agricultural productivity but also promotes resource conservation and environmental sustainability, making it a key component of modern, responsible farming practices.   </div>', unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.divider()
        col1001, col1002, col1003,col1004, col1005 = st.columns([10,10,10,10,15])
        with col1005:
            st.markdown("""
                                <style>
                                @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                                .custom-text-10 { font-family: 'Agdasima', sans-serif; font-size: 28px;color: cyan  }
                                </style>
                                <p class="custom-text-10">An Effort by : MAVERICK_GR </p>
                                """, unsafe_allow_html=True) 
    
    if selected == 'Crop recommendation':
        st.write('')
        st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-12 { font-family: 'Agdasima', sans-serif; font-size: 30px;color:  #e74c3c   }
                    </style>
                    <p class="custom-text-12">Enter the values below for the crop recommendation based on prevailing soil and weather conditions</p>
                    """, unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        col204, col205 = st.columns([12,8])
        with col204:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 30px;color: #82e0aa  }
                    </style>
                    <p class="custom-text-4">Enter the level of Nitrogen in the soil </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write('')
        
        with col205:
            n1 = st.text_input('Ideal value : 0-140', '0')
            n = float(n1)
            if n<0 or n>140:
                st.error('Please enter a value in the specified range', icon="🚨")
            st.write('')
            st.write('')
        st.write('<span style="font-size: 20px;">' + '-' * 144 + '</span>', unsafe_allow_html=True)
        col207, col208 = st.columns([12,8])
        with col207:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 30px;color: #82e0aa  }
                    </style>
                    <p class="custom-text-4">Enter the level of Phosporous in the soil </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write('')
        with col208:
            p1 = st.text_input('Ideal value : 5-145', '5')
            p = float(p1)
            if p<5 or p>145:
                st.error('Please enter a value in the specified range', icon="🚨")
            st.write('')
        st.write('<span style="font-size: 20px;">' + '-' * 144 + '</span>', unsafe_allow_html=True)
        col209, col210 = st.columns([12,8])    
        with col209:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 30px;color: #82e0aa  }
                    </style>
                    <p class="custom-text-4">Enter the level of Potassium in the soil </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write('')
        with col210:
            k1 = st.text_input('Ideal value : 5-205', '5')
            k = float(k1)
            if k<5 or k>205:
                st.error('Please enter a value in the specified range', icon="🚨")
            st.write('')
            st.write('')
        st.write('<span style="font-size: 20px;">' + '-' * 144 + '</span>', unsafe_allow_html=True)
        col211, col212 = st.columns([12,8])
        with col211:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 30px;color: #82e0aa  }
                    </style>
                    <p class="custom-text-4">Enter the value of temperature in degree celsius </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write('')
          
        with col212:
            t1 = st.text_input('Ideal value : 8-44', '8')
            t = float(t1)
            if t<8 or t>44:
                st.error('Please enter a value in the specified range', icon="🚨")
            st.write('')
            st.write('')
            #st.write('')
        st.write('<span style="font-size: 20px;">' + '-' * 144 + '</span>', unsafe_allow_html=True)
        col213, col214 = st.columns([12,8])    
        with col213:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 30px;color: #82e0aa  }
                    </style>
                    <p class="custom-text-4">Enter the value of humidity in % </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write('')
        with col214:
            h1 = st.text_input('Ideal value : 14-100', '14')
            h = float(h1)
            if h<14 or h>100:
                st.error('Please enter a value in the specified range', icon="🚨")
            st.write('')
            
        st.write('<span style="font-size: 20px;">' + '-' * 144 + '</span>', unsafe_allow_html=True)
        col215, col216 = st.columns([12,8])    
        with col215:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 30px;color: #82e0aa  }
                    </style>
                    <p class="custom-text-4">Enter the pH value </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write('')
        with col216:
            ph1 = st.text_input('Ideal value : 3-10', '3')
            ph = float(ph1)
            if ph<3 or ph>10:
                st.error('Please enter a value in the specified range', icon="🚨")
            st.write('')
        st.write('<span style="font-size: 20px;">' + '-' * 144 + '</span>', unsafe_allow_html=True)
        col217, col218 = st.columns([12,8])    
        with col217:
            st.markdown("""
                    <style>
                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                    .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 30px;color: #82e0aa  }
                    </style>
                    <p class="custom-text-4">Enter the value of rainfall in mm </p>
                    """, unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.write('')
        with col218:
            r1 = st.text_input('Ideal value : 20-300', '20')
            r = float(r1)
            if r<20 or r>300:
                st.error('Please enter a value in the specified range', icon="🚨")
            st.write('')
            st.write('')
        st.write('<span style="font-size: 20px;">' + '-' * 144 + '</span>', unsafe_allow_html=True)
        
        if st.button('Suggest a crop based on the above soil and weather conditions', use_container_width=True):
            df = pd.read_csv('Crop_recommendation.csv')
            n1 = (n-df['N'].mean())/df['N'].std()
            p1 = (p-df['P'].mean())/df['P'].std()
            k1 = (k-df['K'].mean())/df['K'].std()
            t1 = (t-df['temperature'].mean())/df['temperature'].std()
            h1 = (h-df['humidity'].mean())/df['humidity'].std()
            ph1 = (ph-df['ph'].mean())/df['ph'].std()
            r1 = (r-df['rainfall'].mean())/df['rainfall'].std()
            #st.write(n1, p1,k1,t1,h1,ph1,r1)
            list2 = [n1, p1,k1,t1,h1,ph1,r1]
            crop1 = predict([list2])
            crop = crop1[0]
            #st.markdown(crop)
            st.write('')
            st.write('')
            if crop == 'apple':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Apple </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Apple.jpg')
            if crop == 'banana':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Banana </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Banana.jpg')
            
            if crop == 'blackgram':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Blackgram </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Blackgram.jpg')
            st.write('')
            st.write('')
            if crop == 'chickpea':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Chickpea </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Chickpea.jpg')
            
            if crop == 'coconut':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Coconut </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Coconut.jpg')
            
            if crop == 'coffee':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Coffee </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Coffee.jpg')
            
            if crop == 'cotton':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Cotton </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Cotton.jpg')
            
            if crop == 'grapes':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Grapes </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Grapes.jpg')
            
            if crop == 'jute':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Jute </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Jute.jpg')
            
            if crop == 'kidneybeans':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Kidneybeans </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Kidneybeans.jpg')
            
            if crop == 'lentil':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f  }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Lentil </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Lentil.jpg')
            
            if crop == 'maize':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Maize </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Maize.jpg')
            
            if crop == 'mango':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Mango </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Mango.jpg')
            
            if crop == 'mothbeans':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Mothbeans </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Mothbeans.jpg')
            
            if crop == 'mungbean':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Mungbean </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Mungbean.jpg')
            
            if crop == 'muskmelon':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Muskmelon </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Muskmelon.jpg')
            
            if crop == 'orange':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Orange </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Orange.jpg')
            
            if crop == 'papaya':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Papaya </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Papaya.jpg')
            
            if crop == 'pigeonpeas':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Pigeonpeas </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Pigeonpeas.jpg')
            
            if crop == 'pomegranate':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Pomegranate </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Pomegranate.jpg')
            
            if crop == 'rice':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Rice </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Rice.jpg')
            
            if crop == 'watermelon':
                col301, col302 = st.columns([12,3])
                with col301:
                    st.markdown("""
                        <style>
                        @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                        .custom-text-4 { font-family: 'Agdasima', sans-serif; font-size: 40px;color:  #f1c40f   }
                        </style>
                        <p class="custom-text-4"> The crop ideal for the above mentioned conditions is : Watermelon </p>
                        """, unsafe_allow_html=True)
                with col302:
                    st.image('Watermelon.jpg')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.divider()
        col1001, col1002, col1003,col1004, col1005 = st.columns([10,10,10,10,15])
        with col1005:
            st.markdown("""
                                <style>
                                @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                                .custom-text-15 { font-family: 'Agdasima', sans-serif; font-size: 28px;color:  #f1c40f   }
                                </style>
                                <p class="custom-text-15">An Effort by : MAVERICK_GR </p>
                                """, unsafe_allow_html=True) 
    
    if selected == 'Developer contact details':
        st.divider()
        col301, col302 = st.columns([10,20])
        with col301:
            st.markdown(":orange[email id:]")
            st.write('')
        with col302:
            st.markdown(":yellow[gururaj008@gmail.com]")
            st.write('')

        col301, col302 = st.columns([10,20])
        with col301:
            st.markdown(":orange[Personal webpage hosting Datascience projects :]")
            st.write('')
        with col302:
            st.markdown(":yellow[https://gururaj-hc-personal-webpage.streamlit.app/]")
            st.write('')

        col301, col302 = st.columns([10,20])
        with col301:
            st.markdown(":orange[LinkedIn profile :]")
            st.write('')
        with col302:
            st.markdown(":yellow[https://www.linkedin.com/in/gururaj-hc-data-science-enthusiast/]")
            st.write('')


        col301, col302 = st.columns([10,20])
        with col301:
            st.markdown(":orange[Github link:]")
            st.write('')
        with col302:
            st.markdown(":yellow[https://github.com/Gururaj008]")
            st.write('')

                
                
        st.divider()
        col1001, col1002, col1003,col1004, col1005 = st.columns([10,10,10,10,15])
        with col1005:
            st.markdown("""
                                    <style>
                                    @import url('https://fonts.googleapis.com/css2?family=Agdasima');
                                    .custom-text-20 { font-family: 'Agdasima', sans-serif; font-size: 28px;color:   #d7bde2   }
                                    </style>
                                    <p class="custom-text-20">An Effort by : _MAVERICK_GR_</p>
                                    """, unsafe_allow_html=True)

            

        
