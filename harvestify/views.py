from django.http import HttpResponse, response
from django.shortcuts import render
import numpy as np
from django.shortcuts import render
from keras.preprocessing.image import img_to_array, load_img
import joblib
import numpy as np
from django.core.files.storage import default_storage
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array, load_img
from keras.models import model_from_json
import tensorflow as tf

model = tf.lite.TFLiteConverter.from_keras_model('detect_model.h5')
#model = tf.keras.models.load_model('detect_model.h5')
#load json and create model
#json_file = open('Cnn_model.json', 'r')
#loaded_model_json = json_file.read()
#json_file.close()
#model = model_from_json(loaded_model_json)
# load weights into new model
#model.load_weights("Cnn_weights.h5")
#print("Loaded model from disk")
#model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

disease_classes = ['Apple___Apple_scab',
                   'Apple___Black_rot',
                   'Apple___Cedar_apple_rust',
                   'Apple___healthy',
                   'Blueberry___healthy',
                   'Cherry_(including_sour)___Powdery_mildew',
                   'Cherry_(including_sour)___healthy',
                   'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                   'Corn_(maize)___Common_rust_',
                   'Corn_(maize)___Northern_Leaf_Blight',
                   'Corn_(maize)___healthy',
                   'Grape___Black_rot',
                   'Grape___Esca_(Black_Measles)',
                   'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Grape___healthy',
                   'Orange___Haunglongbing_(Citrus_greening)',
                   'Peach___Bacterial_spot',
                   'Peach___healthy',
                   'Pepper,_bell___Bacterial_spot',
                   'Pepper,_bell___healthy',
                   'Potato___Early_blight',
                   'Potato___Late_blight',
                   'Potato___healthy',
                   'Raspberry___healthy',
                   'Soybean___healthy',
                   'Squash___Powdery_mildew',
                   'Strawberry___Leaf_scorch',
                   'Strawberry___healthy',
                   'Tomato___Bacterial_spot',
                   'Tomato___Early_blight',
                   'Tomato___Late_blight',
                   'Tomato___Leaf_Mold',
                   'Tomato___Septoria_leaf_spot',
                   'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Target_Spot',
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                   'Tomato___Tomato_mosaic_virus',
                   'Tomato___healthy']

def home(request):
    return render(request, 'home.html')

def detect(request):

    if request.method == "POST":
        file = request.FILES["sentFile"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)

        test_image = load_img(file_url, target_size=(256, 256))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        predictions = model.predict_classes(test_image)
        label = disease_classes[predictions[0]]
        print('label :', label)

        if label  == 'Apple___Apple_scab':
            str="""Crop : Apple\n\n\
                   Disease : Apple Scab\n\n\
                   Cause of disease :
                   1. Apple scab overwinters primarily in fallen leaves and in the soil. Disease development is favored by wet, cool weather that generally occurs in spring and early summer.
                   2. Fungal spores are carried by wind, rain or splashing water from the ground to flowers, leaves or fruit. During damp or rainy periods, newly opening apple leaves are extremely susceptible to infection. The longer the leaves remain wet, the more severe the infection will be. Apple scab spreads rapidly between 55-75 degrees Fahrenheit.\n\n\
                   How to prevent/cure the disease :
                   1. Choose resistant varieties when possible.
                   2. Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring.
                   3. Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.
                   4. Spread a 3- to 6-inch layer of compost under trees, keeping it away from the trunk, to cover soil and prevent splash dispersal of the fungal spores."""
            disease = str
            print(str)

        if label  == 'Apple___Black_rot':
            str="""Crop : Apple\n\n\ 
                   Disease : Black Rot\n\n\
                   Cause of disease :
                   Black rot is caused by the fungus Diplodia seriata (syn Botryosphaeria obtusa).The fungus can infect dead tissue as well as living trunks, branches, leaves and fruits. In wet weather, spores are released from these infections and spread by wind or splashing water. The fungus infects leaves and fruit through natural openings or minor wounds.\n\n\
                   How to prevent/cure the disease :
                   1. Prune out dead or diseased branches.
                   2. Prune out dead or diseased branches.
                   3. Remove infected plant material from the area.
                   4. Remove infected plant material from the area.
                   5. Be sure to remove the stumps of any apple trees you cut down. Dead stumps can be a source of spores."""
            disease = str
            print(str)
        
        if label  == 'Apple___Cedar_apple_rust':
            str="""Crop : Apple\n\n\
                   Disease : Cedar Apple Rust\n\n\
                   Cause of disease :  Cedar apple rust (Gymnosporangium juniperi-virginianae) is a fungal disease that depends on two species to spread and develop. It spends a portion of its two-year life cycle on Eastern red cedar (Juniperus virginiana). The pathogen’s spores develop in late fall on the juniper as a reddish brown gall on young branches of the trees.\n\n\
                   How to prevent/cure the disease :
                   1. Since the juniper galls are the source of the spores that infect the apple trees, cutting them is a sound strategy if there aren’t too many of them.
                   2. While the spores can travel for miles, most of the ones that could infect your tree are within a few hundred feet.
                   3. The best way to do this is to prune the branches about 4-6 inches below the galls."""
            disease = str
            print(str)

        if label  == 'Apple___healthy':
            str="""Crop : Apple\n\n\
                   Disease : No disease"""
            disease = str
            print(str)
        
        if label  == 'Blueberry___healthy':
            str="""Crop : Blueberry\n\n\
                   Disease : No disease"""
            disease = str
            print(str)
        
        if label  == 'Cherry_(including_sour)___Powdery_mildew':
            str="""Crop : Cherry\n\n\
                   Disease : Powdery Mildew\n\n\
                   Cause of disease :\n\n\
                   Podosphaera clandestina, a fungus that most commonly infects young, expanding leaves but can also be found on buds, fruit and fruit stems. It overwinters as small, round, black bodies (chasmothecia) on dead leaves, on the orchard floor, or in tree crotches. Colonies produce more (asexual) spores generally around shuck fall and continue the disease cycle.\n\n\
                   How to prevent/cure the disease :
                   1. Remove and destroy sucker shoots.
                   2. Keep irrigation water off developing fruit and leaves by using irrigation that does not wet the leaves. Also, keep irrigation sets as short as possible.
                   3. Follow cultural practices that promote good air circulation, such as pruning, and moderate shoot growth through judicious nitrogen management."""
            disease = str
            print(str)

        if label  == 'Cherry_(including_sour)___healthy':
            str="""Crop : Cherry\n\n\
                   Disease : No disease"""
            disease = str
            print(str)

        if label  == 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot':
            str="""Crop : Corn\n\n\
                    Disease : Grey Leaf Spot\n\n\
                    Cause of disease :
                    Gray leaf spot lesions on corn leaves hinder photosynthetic activity, reducing carbohydrates allocated towards grain fill. The extent to which gray leaf spot damages crop yields can be estimated based on the extent to which leaves are infected relative to grainfill. Damage can be more severe when developing lesions progress past the ear leaf around pollination time.	Because a decrease in functioning leaf area limits photosynthates dedicated towards grainfill, the plant might mobilize more carbohydrates from the stalk to fill kernels.\n\n\
                    How to prevent/cure the disease : 
                    1. In order to best prevent and manage corn grey leaf spot, the overall approach is to reduce the rate of disease growth and expansion.
                    2. This is done by limiting the amount of secondary disease cycles and protecting leaf area from damage until after corn grain formation.
                    3. High risk factors for grey leaf spot in corn: 
                        a.	Susceptible hybrid
                        b.	Continuous corn
                        c.	Late planting date
                        d.	Minimum tillage systems
                        e.	Field history of severe disease
                        f.	Early disease activity (before tasseling)
                        g.	Irrigation
                        h.	Favorable weather forecast for disease."""
            disease = str
            print(str)

        if label  == 'Corn_(maize)___Common_rust_':
            str="""Crop : Corn(maize)\n\n\
                   Disease : Common Rust\n\n\
                   Cause of disease :
                   Common corn rust, caused by the fungus Puccinia sorghi, is the most frequently occurring of the two primary rust diseases of corn in the U.S., but it rarely causes significant yield losses in Ohio field (dent) corn. Occasionally field corn, particularly in the southern half of the state, does become severely affected when weather conditions favor the development and spread of rust fungus.\n\n\
                   How to prevent/cure the disease : 
                   1. Although rust is frequently found on corn in Ohio, very rarely has there been a need for fungicide applications. This is due to the fact that there are highly resistant field corn hybrids available and most possess some degree of resistance.
                   2. However, popcorn and sweet corn can be quite susceptible. In seasons where considerable rust is present on the lower leaves prior to silking and the weather is unseasonably cool and wet, an early fungicide application may be necessary for effective disease control. Numerous fungicides are available for rust control."""
            disease = str
            print(str)

        if label  == 'Corn_(maize)___Northern_Leaf_Blight':
            str="""Crop : Corn(maize)\n\n\
                   Disease : Northern Leaf Blight\n\n\
                   Cause of disease :
                   Northern corn leaf blight (NCLB) is a foliar disease of corn (maize) caused by Exserohilum turcicum, the anamorph of the ascomycete Setosphaeria turcica. With its characteristic cigar-shaped lesions, this disease can cause significant yield loss in susceptible corn hybrids.\n\n\
                   How to prevent/cure the disease :
                   1. Management of NCLB can be achieved primarily by using hybrids with resistance, but because resistance may not be complete or may fail, it is advantageous to utilize an integrated approach with different cropping practices and fungicides.
                   2. Scouting fields and monitoring local conditions is vital to control this disease."""
            disease = str
            print(str)

        if label  == 'Corn_(maize)___healthy':
            str="""Crop : Corn(maize)\n\n\
                   Disease : No disease """
            disease = str
            print(str)

        if label  == 'Grape___Black_rot':
            str= """Crop : Grape\n\n\
                    Disease : Black Rot\n\n\
                    Cause of disease :
                    1. The black rot fungus overwinters in canes, tendrils, and leaves on the grape vine and on the ground. Mummified berries on the ground or those that are still clinging to the vines become the major infection source the following spring.
                    2. During rain, microscopic spores (ascospores) are shot out of numerous, black fruiting bodies (perithecia) and are carried by air currents to young, expanding leaves. In the presence of moisture, these spores germinate in 36 to 48 hours and eventually penetrate the leaves and fruit stems. 
                    3. The infection becomes visible after 8 to 25 days. When the weather is wet, spores can be released the entire spring and summer providing continuous infection\n\n\
                    How to prevent/cure the disease :
                    1. Space vines properly and choose a planting site where the vines will be exposed to full sun and good air circulation. Keep the vines off the ground and insure they are properly tied, limiting the amount of time the vines remain wet thus reducing infection.
                    2. Keep the fruit planting and surrounding areas free of weeds and tall grass. This practice will promote lower relative humidity and rapid drying of vines and thereby limit fungal infection.
                    3. Use protective fungicide sprays. Pesticides registered to protect the developing new growth include copper, captan, ferbam, mancozeb, maneb, triadimefon, and ziram. Important spraying times are as new shoots are 2 to 4 inches long, and again when they are 10 to 15 inches long, just before bloom, just after bloom, and when the fruit has set."""
            disease = str
            print(str)

        if label  == 'Grape___Esca_(Black_Measles)':
            str="""Crop : Grape\n\n\
                   Disease : Black Measle\n\n\
                   Cause of disease :
                   1. Black Measles is caused by a complex of fungi that includes several species of Phaeoacremonium, primarily by P. aleophilum (currently known by the name of its sexual stage, Togninia minima), and by Phaeomoniella chlamydospora.
                   2. The overwintering structures that produce spores (perithecia or pycnidia, depending on the pathogen) are embedded in diseased woody parts of vines. The overwintering structures that produce spores (perithecia or pycnidia, depending on the pathogen) are embedded in diseased woody parts of vines.
                   3. During fall to spring rainfall, spores are released and wounds made by dormant pruning provide infection sites.
                   4. Wounds may remain susceptible to infection for several weeks after pruning with susceptibility declining over time.\n\n\
                   How to prevent/cure the disease : 
                   1. Post-infection practices (sanitation and vine surgery) for use in diseased, mature vineyards are not as effective and are far more costly than adopting preventative practices (delayed pruning, double pruning, and applications of pruning-wound protectants) in young vineyards. 
                   2. Sanitation and vine surgery may help maintain yields. In spring, look for dead spurs or for stunted shoots. Later in summer, when there is a reduced chance of rainfall, practice good sanitation by cutting off these cankered portions of the vine beyond the canker, to where wood appears healthy. Then remove diseased, woody debris from the vineyard and destroy it.
                   3. The fungicides labeled as pruning-wound protectants, consider using alternative materials, such as a wound sealant with 5 percent boric acid in acrylic paint (Tech-Gro B-Lock), which is effective against Eutypa dieback and Esca, or an essential oil (Safecoat VitiSeal)."""
            disease = str
            print(str)

        if label  == 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)':
            str="""Crop : Grape\n\n\
                   Disease : Leaf Blight\n\n\
                   Cause of disease :
                   1. Apple scab overwinters primarily in fallen leaves and in the soil. Disease development is favored by wet, cool weather that generally occurs in spring and early summer.
                   2. Fungal spores are carried by wind, rain or splashing water from the ground to flowers, leaves or fruit. During damp or rainy periods, newly opening apple leaves are extremely susceptible to infection. The longer the leaves remain wet, the more severe the infection will be. Apple scab spreads rapidly between 55-75 degrees Fahrenheit.\n\n\
                   How to prevent/cure the disease  
                   1. Choose resistant varieties when possible.
                   2. Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring
                   3. Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur.
                   4. Spread a 3- to 6-inch layer of compost under trees, keeping it away from the trunk, to cover soil and prevent splash dispersal of the fungal spores."""
            disease = str
            print(str)

        if label  == 'Grape___healthy':
            str= """Crop : Grape\n\n\
                    Disease : No disease""" 
            disease = str
            print(str)

        if label  == 'Orange___Haunglongbing_(Citrus_greening)':
            str="""Crop : Orange\n\n\
                   Disease : Citrus Greening\n\n\
                   Cause of disease :
                   Huanglongbing (HLB) or citrus greening is the most severe citrus disease, currently devastating the citrus industry worldwide. The presumed causal bacterial agent Candidatus Liberibacter spp. affects tree health as well as fruit development, ripening and quality of citrus fruits and juice.\n\n\
                   How to prevent/cure the disease :
                   1. In regions where disease incidence is low, the most common practices are avoiding the spread of infection by removal of symptomatic trees, protecting grove edges through intensive monitoring, use of pesticides, and biological control of the vector ACP.
                   2. According to Singerman and Useche (2016), CHMAs coordinate insecticide application to control the ACP spreading across area-wide neighboring commercial citrus groves as part of a plan to address the HLB disease.
                   3. In addition to foliar nutritional sprays, plant growth regulators were tested, unsuccessfully, to reduce HLB-associated fruit drop (Albrigo and Stover, 2015)."""
            disease = str
            print(str)

        if label  == 'Peach___Bacterial_spot':
            str="""Crop : Peach\n\n\
                    Disease : Bacterial Spot\n\n\
                    Cause of disease :
                    1. The disease is caused by four species of Xanthomonas (X. euvesicatoria, X. gardneri, X. perforans, and X. vesicatoria). In North Carolina, X. perforans is the predominant species associated with bacterial spot on tomato and X. euvesicatoria is the predominant species associated with the disease on pepper.
                    2. All four bacteria are strictly aerobic, gram-negative rods with a long whip-like flagellum (tail) that allows them to move in water, which allows them to invade wet plant tissue and cause infection.\n\n\
                    How to prevent/cure the disease :  
                    1. The most effective management strategy is the use of pathogen-free certified seeds and disease-free transplants to prevent the introduction of the pathogen into greenhouses and field production areas. Inspect plants very carefully and reject infected transplants- including your own!
                    2. In transplant production greenhouses, minimize overwatering and handling of seedlings when they are wet.
                    3. Trays, benches, tools, and greenhouse structures should be washed and sanitized between seedlings crops.
                    4. Do not spray, tie, harvest, or handle wet plants as that can spread the disease."""
            disease = str
            print(str)

        if label  == 'Peach___healthy':
            str="""Crop : Peach\n\n\
                   Disease : No disease"""
            disease = str
            print(str)

        if label  == 'Pepper,_bell___Bacterial_spot':
            str="""Crop : Pepper\n\n\
                   Disease : Bacterial Spot\n\n\
                   Cause of disease:
                   1. Bacterial spot is caused by several species of gram-negative bacteria in the genus Xanthomonas.
                   2. In culture, these bacteria produce yellow, mucoid colonies. A "mass" of bacteria can be observed oozing from a lesion by making a cross-sectional cut through a leaf lesion, placing the tissue in a droplet of water, placing a cover-slip over the sample, and examining it with a microscope (~200X).\n\n\
                   How to prevent/cure the disease :
                   1. The primary management strategy of bacterial spot begins with use of certified pathogen-free seed and disease-free transplants.
                   2. The bacteria do not survive well once host material has decayed, so crop rotation is recommended. Once the bacteria are introduced into a field or greenhouse, the disease is very difficult to control.
                   3. Pepper plants are routinely sprayed with copper-containing bactericides to maintain a "protective" cover on the foliage and fruit."""
            disease = str
            print(str)

        if label  == 'Pepper,_bell___healthy':
            str="""Crop : Pepper\n\n\
                   Disease : No disease"""
            disease = str
            print(str)

        if label  == 'Potato___Early_blight':
            str="""Crop : Potato\n\n\
                   Disease : Early Blight\n\n\
                   Cause of disease :
                   1. Early blight (EB) is a disease of potato caused by the fungus Alternaria solani. It is found wherever potatoes are grown. 
                   2. The disease primarily affects leaves and stems, but under favorable weather conditions, and if left uncontrolled, can result in considerable defoliation and enhance the chance for tuber infection. Premature defoliation may lead to considerable reduction in yield.
                   3. Primary infection is difficult to predict since EB is less dependent upon specific weather conditions than late blight.\n\n\
                   How to prevent/cure the disease :
                   1. Plant only diseasefree, certified seed. 
                   2. Follow a complete and regular foliar fungicide spray program.
                   3. Practice good killing techniques to lessen tuber infections.
                   4. Allow tubers to mature before digging, dig when vines are dry, not wet, and avoid excessive wounding of potatoes during harvesting and handling."""
            disease = str
            print(str)

        if label  == 'Potato___Late_blight':
            str="""Crop : Potato\n\n\
                   Disease : Late Blight\n\n\
                   Late blight is a potentially devastating disease of potato, infecting leaves, stems and fruits of plants. The disease spreads quickly in fields and can result in total crop failure if untreated. Late blight of potato was responsible for the Irish potato famine of the late 1840s.\n\n\
                   Cause of disease :
                   1. Late blight is caused by the oomycete Phytophthora infestans. Oomycetes are fungus-like organisms also called water molds, but they are not true fungi.
                   2. There are many different strains of P. infestans. These are called clonal lineages and designated by a number code (i.e. US-23). Many clonal lineages affect both tomato and potato, but some lineages are specific to one host or the other.
                   3. The host range is typically limited to potato and tomato, but hairy nightshade (Solanum physalifolium) is a closely related weed that can readily become infected and may contribute to disease spread. Under ideal conditions, such as a greenhouse, petunia also may become infected.\n\n\
                   How to prevent/cure the disease :  
                   1. Seed infection is unlikely on commercially prepared tomato seed or on saved seed that has been thoroughly dried.
                   2. Inspect tomato transplants for late blight symptoms prior to purchase and/or planting, as tomato transplants shipped from southern regions may be infected
                   3. If infection is found in only a few plants within a field, infected plants should be removed, disced-under, killed with herbicide or flame-killed to avoid spreading through the entire field."""
            disease = str
            print(str)

        if label  == 'Potato___healthy':
            str="""Crop : Potato\n\n\
                   Disease : No disease"""
            disease = str
            print(str)

        if label  == 'Raspberry___healthy':
            str="""Crop : Raspberry\n\n\
                   Disease : No disease"""
            disease = str
            print(str)
            
        if label  == 'Soybean___healthy':
            str="""Crop : Soyabean\n\n\
                   Disease : No disease""" 
            disease = str
            print(str)

        if label  == 'Squash___Powdery_mildew':
            str="""Crop : Squash\n\n\
                   Disease : Powdery mildew\n\n\
                   Cause of disease :
                   1. Powdery mildew infections favor humid conditions with temperatures around 68-81° F
                   2. In warm, dry conditions, new spores form and easily spread the disease.
                   3. Symptoms of powdery mildew first appear mid to late summer in Minnesota.  The older leaves are more susceptible and powdery mildew will infect them first.
                   4. Wind blows spores produced in leaf spots to infect other leaves.
                   5. Under favorable conditions, powdery mildew can spread very rapidly, often covering all of the leaves.\n\n\
                   How to prevent/cure the disease :
                   1. Apply fertilizer based on soil test results. Avoid over-applying nitrogen.
                   2. Provide good air movement around plants through proper spacing, staking of plants and weed control.
                   3. Once a week, examine five mature leaves for powdery mildew infection. In large plantings, repeat at 10 different locations in the field.
                   4. If susceptible varieties are growing in an area where powdery mildew has resulted in yield loss in the past, fungicide may be necessary."""
            disease = str
            print(str)

        if label  == 'Strawberry___Leaf_scorch':
            str="""Crop : Strawberry\n\n\
                   Disease : Leaf Scorch\n\n\
                   Cause of disease :
                   1. Scorched strawberry leaves are caused by a fungal infection which affects the foliage of strawberry plantings. The fungus responsible is called Diplocarpon earliana.
                   2. Strawberries with leaf scorch may first show signs of issue with the development of small purplish blemishes that occur on the topside of leaves.\n\n\
                   How to prevent/cure the disease : 
                   1. Since this fungal pathogen over winters on the fallen leaves of infect plants, proper garden sanitation is key.
                   2. This includes the removal of infected garden debris from the strawberry patch, as well as the frequent establishment of new strawberry transplants.
                   3. The avoidance of waterlogged soil and frequent garden cleanup will help to reduce the likelihood of spread of this fungus."""
            disease = str
            print(str)

        if label  == 'Strawberry___healthy':
            str="""Crop : Strawberry\n\n\
                   Disease : No disease""" 
            disease = str
            print(str)

        if label  == 'Tomato___Bacterial_spot':
            str="""Crop : Tomato\n\n\
                   Disease : Bacterial Spot\n\n\
                   Cause of disease :
                   1. The disease is caused by four species of Xanthomonas (X. euvesicatoria, X. gardneri, X. perforans, and X. vesicatoria). In North Carolina, X. perforans is the predominant species associated with bacterial spot on tomato and X. euvesicatoria is the predominant species associated with the disease on pepper.
                   2. All four bacteria are strictly aerobic, gram-negative rods with a long whip-like flagellum (tail) that allows them to move in water, which allows them to invade wet plant tissue and cause infection.\n\n\
                   How to prevent/cure the disease :  
                   1. The most effective management strategy is the use of pathogen-free certified seeds and disease-free transplants to prevent the introduction of the pathogen into greenhouses and field production areas. Inspect plants very carefully and reject infected transplants- including your own!
                   2. In transplant production greenhouses, minimize overwatering and handling of seedlings when they are wet.
                   3. Trays, benches, tools, and greenhouse structures should be washed and sanitized between seedlings crops.
                   4. Do not spray, tie, harvest, or handle wet plants as that can spread the disease"""
            disease = str
            print(str)

        if label  == 'Tomato___Early_blight':
            str="""Crop : Tomato\n\n\
                   Disease : Early Blight\n\n\
                   Cause of disease :
                   1. Early blight can be caused by two different closely related fungi, Alternaria tomatophila and Alternaria solani.
                   2. Alternaria tomatophila is more virulent on tomato than A. solani, so in regions where A. tomatophila is found, it is the primary cause of early blight on tomato. However, if A.tomatophila is absent, A.solani will cause early blight on tomato.\n\n\
                   How to prevent/cure the disease :
                   1. Use pathogen-free seed, or collect seed only from disease-free plants..
                   2. Rotate out of tomatoes and related crops for at least two years.
                   3. Control susceptible weeds such as black nightshade and hairy nightshade, and volunteer tomato plants throughout the rotation.
                   4. Fertilize properly to maintain vigorous plant growth. Particularly, do not over-fertilize with potassium and maintain adequate levels of both nitrogen and phosphorus.
                   5. Avoid working in plants when they are wet from rain, irrigation, or dew.
                   6. Use drip irrigation instead of overhead irrigation to keep foliage dry."""
            disease = str
            print(str)

        if label  == 'Tomato___Late_blight':
            str="""Crop : Tomato\n\n\
                   Disease : Late Blight\n\n\
                   Late blight is a potentially devastating disease of tomato, infecting leaves, stems and fruits of plants. The disease spreads quickly in fields and can result in total crop failure if untreated.\n\n\
                   Cause of disease :
                   1. Late blight is caused by the oomycete Phytophthora infestans. Oomycetes are fungus-like organisms also called water molds, but they are not true fungi.
                   2. There are many different strains of P. infestans. These are called clonal lineages and designated by a number code (i.e. US-23). Many clonal lineages affect both tomato and potato, but some lineages are specific to one host or the other.
                   3. The host range is typically limited to potato and tomato, but hairy nightshade (Solanum physalifolium) is a closely related weed that can readily become infected and may contribute to disease spread. Under ideal conditions, such as a greenhouse, petunia also may become infected."""
            disease = str
            print(str)

        if label  == 'Tomato___Leaf_Mold':
            str="""Crop : Tomato\n\n\
                   Disease : Leaf Mold\n\n\
                   Cause of disease :
                   1. Leaf mold is caused by the fungus Passalora fulva (previously called Fulvia fulva or Cladosporium fulvum). It is not known to be pathogenic on any plant other than tomato.
                   2. Leaf spots grow together and turn brown. Leaves wither and die but often remain attached to the plant.
                   3. Fruit infections start as a smooth black irregular area on the stem end of the fruit. As the disease progresses, the infected area becomes sunken, dry and leathery.\n\n\
                   How to prevent/cure the disease :
                   1. Use drip irrigation and avoid watering foliage.
                   2. Space plants to provide good air movement between rows and individual plants.
                   3. Stake, string or prune to increase airflow in and around the plant.
                   4. Sterilize stakes, ties, trellises etc. with 10 percent household bleach or commercial sanitizer.
                   5. Circulate air in greenhouses or tunnels with vents and fans and by rolling up high tunnel sides to reduce humidity around plants.
                   6. Keep night temperatures in greenhouses higher than outside temperatures to avoid dew formation on the foliage.
                   7. Remove crop residue at the end of the season. Burn it or bury it away from tomato production areas."""
            disease = str
            print(str)

        if label  == 'Tomato___Septoria_leaf_spot':
            str="""Crop : Tomato\n\n\
                   Disease : Leaf Spot\n\n\
                   Cause of disease :
                   Septoria leaf spot is caused by a fungus, Septoria lycopersici. It is one of the most destructive diseases of tomato foliage and is particularly severe in areas where wet, humid weather persists for extended periods.\n\n\
                   How to prevent/cure the disease :  
                   1. Remove diseased leaves.
                   2. Improve air circulation around the plants.
                   3. Mulch around the base of the plants
                   4. Do not use overhead watering.
                   5. Use fungicidal sprayes."""
            disease = str
            print(str)

        if label  == 'Tomato___Spider_mites Two-spotted_spider_mite':
            str="""Crop : Tomato\n\n\
                   Disease : Two-spotted spider mite\n\n\
                   Cause of disease :
                   1. The two-spotted spider mite is the most common mite species that attacks vegetable and fruit crops.
                   2. They have up to 20 generations per year and are favored by excess nitrogen and dry and dusty conditions.
                   3. Outbreaks are often caused by the use of broad-spectrum insecticides which interfere with the numerous natural enemies that help to manage mite populations.\n\n\
                   How to prevent/cure the disease :  
                   1. Avoid early season, broad-spectrum insecticide applications for other pests.
                   2. Do not over-fertilize
                   3. Overhead irrigation or prolonged periods of rain can help reduce populations."""
            disease = str
            print(str)

        if label  == 'Tomato___Target_Spo':
            str=""" Crop : Tomato\n\n\
                    Disease : Target Spot\n\n\
                    Cause of disease :
                    1. The fungus causes plants to lose their leaves; it is a major disease. If infection occurs before the fruit has developed, yields are low.
                    2. This is a common disease on tomato in Pacific island countries. The disease occurs in the screen house and in the field.\n\n\
                    How to prevent/cure the disease :  
                    1. Remove a few branches from the lower part of the plants to allow better airflow at the base
                    2. Remove and burn the lower leaves as soon as the disease is seen, especially after the lower fruit trusses have been picked.
                    3. Keep plots free from weeds, as some may be hosts of the fungus.
                    4. Do not use overhead irrigation; otherwise, it will create conditions for spore production and infection."""
            disease = str
            print(str)

        if label  == 'Tomato___Tomato_Yellow_Leaf_Curl_Virus':
            str="""Crop : Tomato\n\n\
                   Disease : Yellow Leaf Curl Virus\n\n\
                   Cause of disease :
                   1. TYLCV is transmitted by the insect vector Bemisia tabaci in a persistent-circulative nonpropagative manner. The virus can be efficiently transmitted during the adult stages.
                   2. This virus transmission has a short acquisition access period of 15–20 minutes, and latent period of 8–24 hours.\n\n\
                   How to prevent/cure the disease : 
                   1. Currently, the most effective treatments used to control the spread of TYLCV are insecticides and resistant crop varieties.
                   2. The effectiveness of insecticides is not optimal in tropical areas due to whitefly resistance against the insecticides; therefore, insecticides should be alternated or mixed to provide the most effective treatment against virus transmission.
                   3. Other methods to control the spread of TYLCV include planting resistant/tolerant lines, crop rotation, and breeding for resistance of TYLCV. As with many other plant viruses, one of the most promising methods to control TYLCV is the production of transgenic tomato plants resistant to TYLCV."""
            disease = str
            print(str)

        if label  == 'Tomato___Tomato_mosaic_virus':
            str="""  Crop : Tomato\n\n\
                    Disease : Mosaic Virus\n\n\
                    Cause of disease :
                    1. Tomato mosaic virus and tobacco mosaic virus can exist for two years in dry soil or leaf debris, but will only persist one month if soil is moist. The viruses can also survive in infected root debris in the soil for up to two years.
                    2. Seed can be infected and pass the virus to the plant but the disease is usually introduced and spread primarily through human activity. The virus can easily spread between plants on workers' hands, tools, and clothes with normal activities such as plant tying, removing of suckers, and harvest 
                    3. The virus can even survive the tobacco curing process, and can spread from cigarettes and other tobacco products to plant material handled by workers after a cigarette\n\n\
                    How to prevent/cure the disease :  
                    1. Purchase transplants only from reputable sources. Ask about the sanitation procedures they use to prevent disease.
                    2. Inspect transplants prior to purchase. Choose only transplants showing no clear symptoms.
                    3. Avoid planting in fields where tomato root debris is present, as the virus can survive long-term in roots.
                    4. Wash hands with soap and water before and during the handling of plants to reduce potential spread between plants."""
            disease = str
            print(str)

        if label  == 'Tomato___healthy':
            str= """Crop : Tomato\n\n\
                    Disease : No disease"""  
            disease = str
            print(str)

        return render(request, "detect.html", {"predictions": disease})
    else:
        return render(request, "detect.html")

    return render(request, "detect.html")

def crop_recomm(request):

    crop=['apple','banana','blackgram','chickpea','coconut','coffee','cotton','grapes','jute','kidneybeans','lentil', 'maize','mango','mothbeans','mungbean',
        'muskmelon','orange','papaya','pigeonpeas','pomegranate','rice','watermelon']
    random_forest = joblib.load('random_forest_model.sav')
    predlist = []
    
    predlist.append(request.GET.get('n'))
    predlist.append(request.GET.get('p'))
    predlist.append(request.GET.get('k'))
    predlist.append(request.GET.get('temp'))
    predlist.append(request.GET.get('humidity'))
    predlist.append(request.GET.get('ph'))
    predlist.append(request.GET.get('rainfall'))

    if predlist[0] is None and predlist[1] is None and predlist[2] is None and predlist[3] is None and predlist[4] is None and predlist[5] is None and predlist[6] is None:
        return render(request, 'crop_recom.html',{'res':' '})

    data = np.array([predlist])
    print("Data",data)
    new_X = np.nan_to_num(data.astype(np.float32))
    prediction = random_forest.predict(new_X)
    res = crop[prediction[0]]
    print('prediction :', prediction)
    print('res :', res)
    return render(request, 'crop_recom.html',{'res':res})

    
