import re
import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

base_dir = r'c:\Users\caneu\Downloads\caneup-xyz-restore'
post_file = os.path.join(base_dir, 'content', 'posts', 'anoopshahar-sugar-factory-2026.md')

raw_options = """
			<option selected="selected" value="-1">Select Village</option>
			<option value="1">ABHAIPUR (1)</option>
			<option value="2">ACHALPUR (2)</option>
			<option value="3">AENCHORA (3)</option>
			<option value="60712">AHAR (60712)</option>
			<option value="5">AHAR (5)</option>
			<option value="6">AIDALPUR (6)</option>
			<option value="7">AJNARA (7)</option>
			<option value="8">AKARWAS (8)</option>
			<option value="9">AKBARPUR (9)</option>
			<option value="13">AMARGARH (13)</option>
			<option value="579">AMARPUR (579)</option>
			<option value="33499">AMARPUR (33499)</option>
			<option value="16">AMARPUR (16)</option>
			<option value="15">AMARPUR (15)</option>
			<option value="17">AMBA (17)</option>
			<option value="18">AMETHA (18)</option>
			<option value="10">ANASAARAJ (10)</option>
			<option value="19">ANCHURU-KALAN (19)</option>
			<option value="20">ANDHIYAR (20)</option>
			<option value="21">ANIWAS (21)</option>
			<option value="22">ANJANI (22)</option>
			<option value="23">ANOOPSHAHR (23)</option>
			<option value="24">ASADPURGHER (24)</option>
			<option value="25">ASAWARI (25)</option>
			<option value="26">ASHRAFPURBHADAURI (26)</option>
			<option value="27">BACHCHIKHERA (27)</option>
			<option value="28">BADARKHA (28)</option>
			<option value="29">BADARPUR (29)</option>
			<option value="537">BADAUDA (537)</option>
			<option value="31">BADSHAHPUR-PACHGAI (31)</option>
			<option value="32">BAGSARA (32)</option>
			<option value="33">BAGTHARI (33)</option>
			<option value="34">BAHANPUR (34)</option>
			<option value="35">BAHEERKHERA (35)</option>
			<option value="36">BAILON (36)</option>
			<option value="38">BAIRAL (38)</option>
			<option value="40">BAJHERA (40)</option>
			<option value="39">BAJHERA (39)</option>
			<option value="41">BAJIDPUR (41)</option>
			<option value="559">BALDEOGARH (559)</option>
			<option value="42">BAMANPUR (42)</option>
			<option value="46">BANDOR (46)</option>
			<option value="47">BANSURI (47)</option>
			<option value="48">BANWARIPUR (48)</option>
			<option value="50">BARAINA (50)</option>
			<option value="51">BARARI (51)</option>
			<option value="53">BARHA (53)</option>
			<option value="55">BARHPURA (55)</option>
			<option value="56">BARWALA (56)</option>
			<option value="58">BAWANPURTALUKA (58)</option>
			<option value="61">BHADORA (61)</option>
			<option value="62">BHAGWANTPUR (62)</option>
			<option value="63">BHAILAI (63)</option>
			<option value="64">BHAIPUR (64)</option>
			<option value="65">BHAIYANPUR (65)</option>
			<option value="70">BHAW-RAUA (70)</option>
			<option value="71">BHEEMPUR (71)</option>
			<option value="72">BHERIA-HARIDWARPUR (72)</option>
			<option value="74">BHOPATPUR (74)</option>
			<option value="75">BHOPUR (75)</option>
			<option value="77">BICHAULA (77)</option>
			<option value="78">BIDHIPUR (78)</option>
			<option value="81">BILAUNAROOP (81)</option>
			<option value="82">BIRAULY (82)</option>
			<option value="83">BIRAURA (83)</option>
			<option value="84">BIVIYANA (84)</option>
			<option value="85">BOHICH (85)</option>
			<option value="86">BORHA (86)</option>
			<option value="89">BUDHANPUR (89)</option>
			<option value="472">BURHANPUR KHURD (472)</option>
			<option value="92">BURHANPUR-KALAN (92)</option>
			<option value="93">CHACHRAI (93)</option>
			<option value="94">CHAHLA (94)</option>
			<option value="95">CHAKLA (95)</option>
			<option value="514">CHAMERI (514)</option>
			<option value="96">CHANDAUK (96)</option>
			<option value="99">CHARAURIRANIKATYANI (99)</option>
			<option value="100">CHARORA (100)</option>
			<option value="101">CHASI (101)</option>
			<option value="102">CHATHERA (102)</option>
			<option value="104">CHAUGANPUR (104)</option>
			<option value="105">CHAUNDERA (105)</option>
			<option value="107">CHHATURIA (107)</option>
			<option value="108">CHILMAPUR (108)</option>
			<option value="109">CHIMAWALI (109)</option>
			<option value="110">CHIRAURI-TALUKA (110)</option>
			<option value="112">DABKA (112)</option>
			<option value="113">DABKAURA (113)</option>
			<option value="575">DABKAURA ASR (575)</option>
			<option value="114">DADUA-MUSTAFABAD (114)</option>
			<option value="115">DANGARH (115)</option>
			<option value="116">DANPUR (116)</option>
			<option value="119">DARAURA (119)</option>
			<option value="120">DARAWAR (120)</option>
			<option value="122">DARVESHPUR (122)</option>
			<option value="123">DAULATANAGAR (123)</option>
			<option value="125">DAULATPUR (125)</option>
			<option value="126">DAULATPURKHURD (126)</option>
			<option value="127">DAUNKA (127)</option>
			<option value="128">DEBAI (128)</option>
			<option value="130">DEBAI-DEHAT (130)</option>
			<option value="131">DEORAU (131)</option>
			<option value="132">DEVIKANAGLA (132)</option>
			<option value="133">DEVRALA (133)</option>
			<option value="135">DHAKNAGLA (135)</option>
			<option value="134">DHAKNAGLA (134)</option>
			<option value="139">DHALNA (139)</option>
			<option value="573">DHAMANI (573)</option>
			<option value="140">DHARAMPUR (140)</option>
			<option value="141">DHEEMARI (141)</option>
			<option value="143">DHOOSARI-KADARABAD (143)</option>
			<option value="1143">DHOSRI KADRABAD (1143)</option>
			<option value="144">DIRAURABISHWNATHPUR (144)</option>
			<option value="145">DOGAWAN (145)</option>
			<option value="146">DOMALAHASANGARH (146)</option>
			<option value="148">DOONGARAJOGI (148)</option>
			<option value="147">DOONGRAJAT (147)</option>
			<option value="149">DUGRAU (149)</option>
			<option value="150">DULKHARA (150)</option>
			<option value="152">ELANA (152)</option>
			<option value="153">FAIJPURA (153)</option>
			<option value="154">FAREEDPUR (154)</option>
			<option value="155">FARIDA (155)</option>
			<option value="156">FARIDPURHAWELI (156)</option>
			<option value="5097">FATEHGARH (5097)</option>
			<option value="157">FATEHGARHI (157)</option>
			<option value="159">FATEHPUR (159)</option>
			<option value="158">FATEHPUR (158)</option>
			<option value="160">GAHNA (160)</option>
			<option value="161">GALIBPUR (161)</option>
			<option value="162">GANGAGARH (162)</option>
			<option value="163">GANGAPUR (163)</option>
			<option value="164">GANGAWASPAHARA (164)</option>
			<option value="165">GARHARA (165)</option>
			<option value="166">GARIA-SULTANPUR (166)</option>
			<option value="168">GAWAN (168)</option>
			<option value="171">GHOSIPURA (171)</option>
			<option value="174">GHUSRANA HARI SINGH (174)</option>
			<option value="173">GHUSRANAGAIL (173)</option>
			<option value="176">GODHANA (176)</option>
			<option value="177">GODHANA (177)</option>
			<option value="178">GOKALPUR (178)</option>
			<option value="179">GOSHAMI (179)</option>
			<option value="180">GOVINDPUR (180)</option>
			<option value="181">GUCHAWALI (181)</option>
			<option value="182">GURAWALI (182)</option>
			<option value="183">HAMEERPUR (183)</option>
			<option value="184">HARCHANDPUR (184)</option>
			<option value="561">HASANGARHI (561)</option>
			<option value="186">HASANPUR (186)</option>
			<option value="187">HASANPUR-UJARI (187)</option>
			<option value="188">HATAMPUR (188)</option>
			<option value="190">HAZRATPUR (190)</option>
			<option value="191">HEERAPUR-KALAN (191)</option>
			<option value="192">HEERAPUR-KHURD (192)</option>
			<option value="193">HIMMATGARHI (193)</option>
			<option value="194">HIRANBHOORH (194)</option>
			<option value="515">HIRNOT (515)</option>
			<option value="195">HISAWATI (195)</option>
			<option value="196">HUSAINPURA (196)</option>
			<option value="197">ICHHAWARI (197)</option>
			<option value="200">INDAUR (200)</option>
			<option value="201">ISHANPUR (201)</option>
			<option value="203">JADAUL (203)</option>
			<option value="204">JADAULI (204)</option>
			<option value="206">JAHANGIRABAD (206)</option>
			<option value="207">JAIRAM PUR (207)</option>
			<option value="209">JAKHETA (209)</option>
			<option value="210">JALALPUR (210)</option>
			<option value="211">JALALPUR-JATT (211)</option>
			<option value="212">JALALPUR-KARIRA (212)</option>
			<option value="213">JALALPUR-KATORA (213)</option>
			<option value="214">JALEELPUR (214)</option>
			<option value="215">JAMALPUR (215)</option>
			<option value="216">JAMRAU (216)</option>
			<option value="217">JANAURA (217)</option>
			<option value="218">JARAINA (218)</option>
			<option value="219">JARAJPUR (219)</option>
			<option value="220">JARGAWAN (220)</option>
			<option value="222">JASAR (222)</option>
			<option value="223">JATPURA (223)</option>
			<option value="224">JATWAI (224)</option>
			<option value="226">JEEWANPUR (226)</option>
			<option value="227">JINAI (227)</option>
			<option value="228">JIRAULI (228)</option>
			<option value="576">JUGSANA KHURD ASR (576)</option>
			<option value="229">JUGSANAKALAN (229)</option>
			<option value="230">JUGSANAKHURD (230)</option>
			<option value="232">KADARIBAG (232)</option>
			<option value="233">KAKRAI (233)</option>
			<option value="234">KAKRAI-KHERA (234)</option>
			<option value="235">KALA-KHURI (235)</option>
			<option value="236">KALAINA (NON MEMBER) (236)</option>
			<option value="237">KALIYANPUR (237)</option>
			<option value="142">KALYANPUR (142)</option>
			<option value="239">KAMALPUR (239)</option>
			<option value="240">KAMAUTHA (240)</option>
			<option value="242">KANHERA (242)</option>
			<option value="244">KAPSAI (244)</option>
			<option value="245">KAPSAI-BALRAMPUR (245)</option>
			<option value="247">KARAITHA (247)</option>
			<option value="249">KARANPUR-KALA (249)</option>
			<option value="250">KARANSINGHPUR (250)</option>
			<option value="252">KARANWAS (252)</option>
			<option value="253">KARIRI (253)</option>
			<option value="254">KARIYARI (254)</option>
			<option value="255">KARONJI (255)</option>
			<option value="256">KASERKALAN (256)</option>
			<option value="257">KATIYAWALI (257)</option>
			<option value="258">KHADANA (258)</option>
			<option value="259">KHAILIA-KALYANPUR (259)</option>
			<option value="260">KHAIRPUR (260)</option>
			<option value="261">KHAKHOONDA (261)</option>
			<option value="262">KHALAUR (262)</option>
			<option value="263">KHALIKPUR (263)</option>
			<option value="536">KHALSIA (536)</option>
			<option value="264">KHANAUDA-1 (264)</option>
			<option value="265">KHANDOI (265)</option>
			<option value="268">KHANPURA (268)</option>
			<option value="577">KHANPURA ASR (577)</option>
			<option value="269">KHARAKWARI (269)</option>
			<option value="270">KHARWA (270)</option>
			<option value="266">KHAUNAUDA-2 (266)</option>
			<option value="274">KHERIAVAKS (274)</option>
			<option value="275">KHIJARABAD (275)</option>
			<option value="276">KHUDADIA (276)</option>
			<option value="277">KHUSHALABAD (277)</option>
			<option value="278">KHUSHALGARH (278)</option>
			<option value="279">KHUSHARUPUR (279)</option>
			<option value="280">KISHANPUR (280)</option>
			<option value="283">KOTLA (283)</option>
			<option value="284">KUDAINA-JAIRAMPUR (284)</option>
			<option value="285">KUMRAUA (285)</option>
			<option value="286">KURAINA-KOTHARA (286)</option>
			<option value="287">KUSHYA-FATEHABAD (287)</option>
			<option value="544">KUTHAINI (544)</option>
			<option value="288">KUTUBPUR (288)</option>
			<option value="574">KUTUBPUR-A (574)</option>
			<option value="290">KUTUBPUR-NAYAWAS (290)</option>
			<option value="291">LACHHOI (291)</option>
			<option value="294">LAKSHAMPUR (294)</option>
			<option value="295">LAKSHAMPUR (295)</option>
			<option value="296">LODHAI (296)</option>
			<option value="297">LOHARA (297)</option>
			<option value="298">MADANGARH (298)</option>
			<option value="299">MADGAWAN (299)</option>
			<option value="300">MADHOGARH (300)</option>
			<option value="33313">MAGADMA (33313)</option>
			<option value="301">MAHARAJPUR (301)</option>
			<option value="302">MAHARAJPUR-KARKORA (302)</option>
			<option value="305">MAHUAKHERA (305)</option>
			<option value="3077">MALAKPUR (3077)</option>
			<option value="307">MALAKPUR (307)</option>
			<option value="308">MAMAU (308)</option>
			<option value="310">MANAPUR (310)</option>
			<option value="311">MANGALPUR (311)</option>
			<option value="309">MANKARAURA (309)</option>
			<option value="313">MANPUR (313)</option>
			<option value="314">MARHAWALI (314)</option>
			<option value="315">MATHURA-NAGAL (315)</option>
			<option value="316">MAU (316)</option>
			<option value="317">MAUJPUR (317)</option>
			<option value="580">MAUJPUR (580)</option>
			<option value="545">MAUNIPURAURFRAMWAS (545)</option>
			<option value="318">MAWAI (318)</option>
			<option value="319">MEERAPUR (319)</option>
			<option value="320">METHNA-TELIARASULPUR (320)</option>
			<option value="321">MIRZAPURNAGLI (321)</option>
			<option value="325">MOHAMMADPUR-KALAN (325)</option>
			<option value="323">MOHAMMADPURBANGAR (323)</option>
			<option value="324">MOHAMMADPURKHURD (324)</option>
			<option value="326">MOHARSA (326)</option>
			<option value="543">MOODAKHERA (543)</option>
			<option value="330">MUBARAKPUR (330)</option>
			<option value="331">MUBARIKPUR (331)</option>
			<option value="332">MUJAFFARNAGARBAMANI (332)</option>
			<option value="334">MULLANI (334)</option>
			<option value="335">MUMREJPUR (335)</option>
			<option value="337">MURADGARHI (337)</option>
			<option value="336">MURADNAGAR (336)</option>
			<option value="338">MURADPUR (338)</option>
			<option value="558">MURLINAGLA (558)</option>
			<option value="70054">NAGLA BADNAAM SINGH (70054)</option>
			<option value="349">NAGLA KIDDA (349)</option>
			<option value="539">NAGLA ROORH (539)</option>
			<option value="362">NAGLA-BAGSARA (362)</option>
			<option value="363">NAGLA-BHOPATPUR (363)</option>
			<option value="364">NAGLA-CHAPERA-MZMAU (364)</option>
			<option value="568">NAGLA-DANSAHAY (568)</option>
			<option value="343">NAGLA-DHARAKPUR (343)</option>
			<option value="365">NAGLA-FAIJPURA (365)</option>
			<option value="366">NAGLA-GANGAPUR (366)</option>
			<option value="368">NAGLA-MADARIPUR (368)</option>
			<option value="371">NAGLA-NALOO (371)</option>
			<option value="542">NAGLABAGIURFJARGAWA (542)</option>
			<option value="340">NAGLABALURFBALKA (340)</option>
			<option value="341">NAGLABIDHI (341)</option>
			<option value="342">NAGLACHHATTOO (342)</option>
			<option value="344">NAGLAFATTAPUR (344)</option>
			<option value="345">NAGLAGARVI (345)</option>
			<option value="346">NAGLAHARNAMSINGH (346)</option>
			<option value="347">NAGLAHAROOP (347)</option>
			<option value="348">NAGLAJAGAT (348)</option>
			<option value="350">NAGLAKOTHI (350)</option>
			<option value="351">NAGLALODHAI (351)</option>
			<option value="352">NAGLALUFTALIPUR (352)</option>
			<option value="353">NAGLAMAU (353)</option>
			<option value="354">NAGLAMEWATI (354)</option>
			<option value="355">NAGLANAU (355)</option>
			<option value="356">NAGLANOORPUR (356)</option>
			<option value="359">NAGLASHUBHALI (359)</option>
			<option value="360">NAGLATALWAR (360)</option>
			<option value="372">NARAYANPUR (372)</option>
			<option value="373">NARENDRAPUR (373)</option>
			<option value="374">NARORA (374)</option>
			<option value="375">NARSAINA (375)</option>
			<option value="471">NAUDAI-BANGAR (471)</option>
			<option value="548">NAUZARPURBANGAR (548)</option>
			<option value="578">NAVI NAGAR ASR (578)</option>
			<option value="376">NAVINAGAR (376)</option>
			<option value="377">NAVIPURKHERIA (377)</option>
			<option value="379">NAYAWAS-BANGAR (379)</option>
			<option value="381">NEMTABAD (381)</option>
			<option value="382">NGGILLIMZDHARMPUR (382)</option>
			<option value="562">NITYANANDPUR (562)</option>
			<option value="383">NITYANANDPURNAGLI (383)</option>
			<option value="385">NIWARI-BANGAR (385)</option>
			<option value="387">NOORPURNAGLIA (387)</option>
			<option value="388">OKHAND (388)</option>
			<option value="60741">ORANGABAD TAHARPUR (60741)</option>
			<option value="389">ORANGABAD-KASER (389)</option>
			<option value="390">ORANGABAD-TAHARPUR (390)</option>
			<option value="392">PACHADEVRA (392)</option>
			<option value="393">PAGAUNA (393)</option>
			<option value="394">PAHARPUR (394)</option>
			<option value="395">PAHARPURHAWELI (395)</option>
			<option value="396">PAIGAMBARPUR (396)</option>
			<option value="33307">PALIANANDGARHI (33307)</option>
			<option value="397">PALIANANDGARHI (397)</option>
			<option value="553">PARAULI (553)</option>
			<option value="399">PARIHAWALI (399)</option>
			<option value="400">PARLI (400)</option>
			<option value="402">PATRAMPUR (402)</option>
			<option value="403">PAUTH (403)</option>
			<option value="405">PEETAMPUR (405)</option>
			<option value="534">PESARI (534)</option>
			<option value="406">PILAKHANA (406)</option>
			<option value="408">PILAKHANI (408)</option>
			<option value="410">PIPAIRA (410)</option>
			<option value="565">POKHARPUR (565)</option>
			<option value="413">POOTHA (413)</option>
			<option value="414">POOTHARIKALAN (414)</option>
			<option value="415">POTABADSHAHPUR (415)</option>
			<option value="416">PRAKASHPUR (416)</option>
			<option value="33390">PYANA KALAN (33390)</option>
			<option value="417">PYANAKALAN (417)</option>
			<option value="418">PYANAKHURD (418)</option>
			<option value="419">RAGHUNATHPUR (419)</option>
			<option value="420">RAHEEMKOT (420)</option>
			<option value="422">RAHMAPUR (422)</option>
			<option value="421">RAHMAPUR (421)</option>
			<option value="423">RAHMATPUR-OGANA (423)</option>
			<option value="424">RAIPURMAUZAMPUR (424)</option>
			<option value="425">RAJAPUR (425)</option>
			<option value="426">RAJAUR (426)</option>
			<option value="428">RAJGHAT (428)</option>
			<option value="429">RAJPUR (429)</option>
			<option value="430">RAMBILONI (430)</option>
			<option value="432">RAMGHAT (432)</option>
			<option value="431">RAMNAGAR (431)</option>
			<option value="554">RAMNAGAR (554)</option>
			<option value="434">RAMPUR (434)</option>
			<option value="538">RAMPURA (538)</option>
			<option value="560">RAMPURMANPUR (560)</option>
			<option value="436">RAMWAS (436)</option>
			<option value="572">RANAU RAHAM ALIPUR (572)</option>
			<option value="437">RANDHAURA (437)</option>
			<option value="439">RASOOLPUR (439)</option>
			<option value="440">RASULPURNAGLABISAR (440)</option>
			<option value="442">RATANPUR (442)</option>
			<option value="444">RAUNDA (444)</option>
			<option value="445">RETAGARH (445)</option>
			<option value="446">RIWARA (446)</option>
			<option value="449">ROOPASPUR (449)</option>
			<option value="450">ROOPWAS (450)</option>
			<option value="451">ROORHBANGAR (451)</option>
			<option value="452">ROOTHA (452)</option>
			<option value="453">RORA (453)</option>
			<option value="454">ROSHALA (454)</option>
			<option value="455">SABALPUR (455)</option>
			<option value="456">SAHDAWAN (456)</option>
			<option value="458">SALAGWAN (458)</option>
			<option value="460">SALAMATPUR (460)</option>
			<option value="462">SAMANPUR (462)</option>
			<option value="464">SANKHANI (464)</option>
			<option value="535">SARAWA (535)</option>
			<option value="465">SARGAON (465)</option>
			<option value="466">SATOHA (466)</option>
			<option value="468">SATWARA (468)</option>
			<option value="469">SATWARIMAZRASATWARA (469)</option>
			<option value="470">SAUJANARANI (470)</option>
			<option value="473">SENDAFAREEDPUR (473)</option>
			<option value="475">SHABDALPUR (475)</option>
			<option value="476">SHADIPURBANBOI (476)</option>
			<option value="477">SHAFINAGAR (477)</option>
			<option value="478">SHAHJAHANPUR (478)</option>
			<option value="4799">SHAKARPUR (4799)</option>
			<option value="479">SHAKARPUR (479)</option>
			<option value="481">SHEHWAJPURDAULAT (481)</option>
			<option value="484">SHEKHPUR (484)</option>
			<option value="483">SHEKHPUR (483)</option>
			<option value="485">SHEKHPURRAURA (485)</option>
			<option value="487">SHEOPURI (487)</option>
			<option value="488">SHEORAMPUR(GATE) (488)</option>
			<option value="489">SHEORAMPUR(ILNA) (489)</option>
			<option value="490">SHERPUR (490)</option>
			<option value="491">SHERPURBANGAR (491)</option>
			<option value="492">SHIKOI (492)</option>
			<option value="569">SIDDHI NAGLA (569)</option>
			<option value="493">SIHALINAGAR (493)</option>
			<option value="496">SILHARI (496)</option>
			<option value="497">SIRAURA (497)</option>
			<option value="570">SOORAJPUR NISFI (570)</option>
			<option value="499">SORKHA (499)</option>
			<option value="500">SORLA (500)</option>
			<option value="501">SULTANPUR-BILONI (501)</option>
			<option value="502">SUNAI (502)</option>
			<option value="503">SUNANA (503)</option>
			<option value="504">SURAJPUR-MAKHENA (504)</option>
			<option value="505">SURKHUROO (505)</option>
			<option value="507">TAHGAURA (507)</option>
			<option value="508">TAIYABPUR (508)</option>
			<option value="509">TALWAR (509)</option>
			<option value="510">TAULI (510)</option>
			<option value="511">TELIYANAGLA (511)</option>
			<option value="512">THANAGAJROLA (512)</option>
			<option value="516">TITAUTA (516)</option>
			<option value="518">TORAI (518)</option>
			<option value="519">TRILOKPUR (519)</option>
			<option value="520">TULSIGARHI (520)</option>
			<option value="521">UDAIGARHI (521)</option>
			<option value="522">UDAIPURKALAN (522)</option>
			<option value="523">UDAIPURKHURD (523)</option>
			<option value="524">UGAIWA (524)</option>
			<option value="525">UMRARA (525)</option>
			<option value="526">UMRARI (526)</option>
			<option value="527">UNCHAGAON (527)</option>
			<option value="566">UNCHAGAON-KHADAR (566)</option>
			<option value="529">UNISPUR (529)</option>
			<option value="999999">UNKNOWN (999999)</option>
			<option value="530">VEERPUR (530)</option>
			<option value="531">VIJAINAGLIA (531)</option>
			<option value="533">YAWAPUR (533)</option>
"""

matches = re.findall(r'<option value="([^"]+)">([^<]+)</option>', raw_options)
villages = []
for val, text in matches:
    if val == "-1":
        continue
    m_name = re.match(r'^(.*?)\s*\((.*?)\)$', text)
    if m_name:
        name = m_name.group(1).strip()
        code = m_name.group(2).strip()
    else:
        name = text.strip()
        code = val.strip()
    villages.append((name, code))

# Generate HTML table rows
rows_html = ""
for idx, (vname, vcode) in enumerate(villages, 1):
    rows_html += f'  <tr class="vrow"><td>{idx}</td><td class="vname"><strong>{vname}</strong></td><td class="vcode"><code style="background:#dcfce7;color:#15803d;padding:2px 8px;border-radius:4px;font-weight:700;">{vcode}</code></td><td>अनूपशहर चीनी मिल समिति</td></tr>\n'

article_content = f"""---
title: "अनूपशहर चीनी मिल (Anoopshahr Sugar Mill) 2026-27: 453 गांवों की लिस्ट, कोड व पर्ची कैलेंडर गाइड"
date: 2026-08-28T18:30:00+05:30
lastmod: 2026-08-28T18:30:00+05:30
description: "अनूपशहर चीनी मिल (बुलंदशहर/अलीगढ़) से जुड़े सभी 453 गांवों की आधिकारिक लिस्ट और कोड। ऑनलाइन गांव खोजें, पर्ची कैलेंडर, eGanna App डाउनलोड व गन्ना भुगतान स्थिति।"
categories:
- Sugar Mills
tags:
- Anoopshahar Sugar Mill
- अनूपशहर चीनी मिल
- बुलंदशहर गन्ना पर्ची
- eGanna Village List
- CaneUp Village Code
slug: anoopshahar-sugar-factory-2026
ShowToc: true
author: "Randhir Patil"
authors:
- "Randhir Patil"
author_name: "Randhir Patil"
author_image: "/images/authors/randhir-patil.webp"
featured_image: "/images/blog/anoopshahar-sugar-factory-2026.webp"
image: "/images/blog/anoopshahar-sugar-factory-2026.webp"
---

अनूपशहर चीनी मिल (Anoopshahr Sugar Mill) 2026-27: 453 गांवों की लिस्ट, कोड व पर्ची कैलेंडर गाइड

By  
[Randhir Patil](https://caneup.xyz/) - August 28, 2026

**बुलंदशहर/अनूपशहर :** उत्तर प्रदेश के बुलंदशहर जिले की प्रसिद्ध किसान सहकारी चीनी मिल अनूपशहर (Kisan Sahkari Chini Mill Anoopshahr / Wave Sugar Mill) आगामी पेराई सत्र 2026-27 के लिए पूरी तरह तैयार है। यह चीनी मिल बुलंदशहर, अलीगढ़ और संभल जिले की सीमा से सटे लगभग **453 से अधिक गांवों** के गन्ना किसानों से सीधे गन्ने की पेराई करती है। 

यदि आप अनूपशहर चीनी मिल से जुड़े किसान हैं और अपने गांव का आधिकारिक **Village Code (गांव कोड)** खोज रहे हैं, तो नीचे दी गई डायरेक्ट सर्च टेबल का उपयोग करके 1 सेकंड में अपना गांव और कोड जांच सकते हैं।

---

## 🔍 अनूपशहर चीनी मिल — गांव और कोड तुरंत खोजें (Live Village Search)

नीचे दिए गए सर्च बॉक्स में अपने **गांव का नाम (जैसे: AHAR, DEBAI, DANPUR, NARORA, UNCHAGAON)** या **गांव कोड (जैसे: 1, 23, 128, 374)** टाइप करें:

<div style="margin:20px 0;background:#f0fdf4;border:2px solid #bbf7d0;border-radius:12px;padding:16px;">
  <label for="vsearch" style="font-weight:700;color:#15803d;display:block;margin-bottom:8px;font-size:15px;">🔎 अपने गांव का नाम या कोड लिखें:</label>
  <input type="text" id="vsearch" placeholder="उदा. AHAR, DEBAI, NARORA, 128..." onkeyup="filterVillages()" style="width:100%;padding:10px 14px;border:1px solid #15803d;border-radius:8px;font-size:15px;outline:none;">
  <small style="color:#6b7280;display:block;margin-top:6px;">कुल 453 गांव सूचीबद्ध हैं। टाइप करते ही परिणाम नीचे दिखेंगे।</small>
</div>

<div class="tbl-wrap">
<table id="vtable">
<thead>
  <tr>
    <th>#</th>
    <th>गांव का नाम (Village Name)</th>
    <th>गांव कोड (Village Code)</th>
    <th>गन्ना समिति / मिल</th>
  </tr>
</thead>
<tbody>
{rows_html}
</tbody>
</table>
</div>

<script>
function filterVillages() {{
  var input = document.getElementById("vsearch");
  var filter = input.value.toUpperCase();
  var table = document.getElementById("vtable");
  var tr = table.getElementsByTagName("tr");
  for (var i = 1; i < tr.length; i++) {{
    var tdName = tr[i].getElementsByClassName("vname")[0];
    var tdCode = tr[i].getElementsByClassName("vcode")[0];
    if (tdName || tdCode) {{
      var txtName = tdName.textContent || tdName.innerText;
      var txtCode = tdCode.textContent || tdCode.innerText;
      if (txtName.toUpperCase().indexOf(filter) > -1 || txtCode.toUpperCase().indexOf(filter) > -1) {{
        tr[i].style.display = "";
      }} else {{
        tr[i].style.display = "none";
      }}
    }}
  }}
}}
</script>

---

## 🏭 Anoopshahr Sugar Mill Overview & Technical Specifications

| विवरण (Parameter) | आधिकारिक जानकारी (Official Details) |
|---|---|
| **मिल का नाम** | किसान सहकारी चीनी मिल अनूपशहर (Anoopshahr Sugar Mill) |
| **स्थान व जिला** | अनूपशहर, जिला बुलंदशहर, उत्तर प्रदेश |
| **फैक्ट्री कोड (Factory Code)** | 23 (CaneUp Portal) |
| **प्रतिदिन पेराई क्षमता (Crushing Capacity)** | 6,000 TCD (टन प्रति दिन) |
| **संबद्ध कुल गांव (Total Villages)** | **453 गांव** |
| **पेराई सत्र 2026-27 प्रारंभ तिथि** | **15 अक्टूबर से 20 अक्टूबर 2026** |
| **औसत गन्ना भुगतान समय** | 14 दिनों के भीतर (Direct DBT to Bank) |
| **आधिकारिक पोर्टल** | [enquiry.caneup.in](https://enquiry.caneup.in/) |

---

## 📲 CaneUp व eGanna App पर अनूपशहर मिल की पर्ची कैलेंडर कैसे देखें?

अनूपशहर चीनी मिल के सभी किसान भाई अपने मोबाइल से घर बैठे अपनी सप्लाय पर्ची और कैलेंडर जांच सकते हैं:

1. **CaneUp पोर्टल खोलें:** मोबाइल या कंप्यूटर पर **[enquiry.caneup.in](https://enquiry.caneup.in/)** पर जाएं।
2. **कैप्चा कोड दर्ज करें:** स्क्रीन पर दिख रहा Captcha Code डालकर 'Submit' करें।
3. **जिला व मिल चुनें:** 
   - **District:** Bulandshahr (बुलंदशहर)
   - **Factory:** Anoopshahr (अनूपशहर)
4. **गांव व किसान कोड चुनें:**
   - ऊपर दी गई सूची से अपना **Village Code** चुनें (उदा. अनूपशहर शहर का कोड `23` या डिबाई का कोड `128`)।
   - अपना **Grower Code (किसान कोड)** दर्ज करें।
5. **Pre-Calendar & Supply Ticket:** आपके सामने 12 पखवाड़ों की कुल पर्चियों का ब्यौरा आ जाएगा।

---

## 💳 अनूपशहर चीनी मिल गन्ना भुगतान स्थिति (Payment Status 2026)

उत्तर प्रदेश शासन के निर्देशानुसार, अनूपशहर चीनी मिल द्वारा चीनी और एथेनॉल की कुल बिक्री का 85 प्रतिशत हिस्सा सीधे [Escrow Account](https://caneup.xyz/news/breaking-sugar-quota-22-lmt-mill-warning-august-2026/) में जमा कराया जा रहा है। 

- **14 दिनों में भुगतान:** नियमानुसार गन्ने की आपूर्ति के 14 दिनों के भीतर भुगतान सीधे किसान के Aadhaar Seeded Bank Account में DBT द्वारा हस्तांतरित होता है।
- **ब्याज का नियम:** यदि भुगतान 14 दिनों से अधिक विलंबित होता है, तो चीनी मिल को यूपी गन्ना अधिनियम की धारा 17(3) के तहत 15% वार्षिक ब्याज देना होगा।

---

## ❓ अक्सर पूछे जाने वाले सवाल (Frequently Asked Questions)

### Q1. अनूपशहर चीनी मिल का फैक्ट्री कोड (Factory Code) क्या है?
CaneUp पोर्टल और eGanna App पर अनूपशहर चीनी मिल का आधिकारिक फैक्ट्री कोड **23** (या समिति कोड) है।

### Q2. यदि मेरे गांव का नाम इस सूची में नहीं है तो क्या करें?
यदि आपका गांव अनूपशहर मिल के अंतर्गत आता है लेकिन कोड नहीं मिल रहा, तो आप अपने नजदीकी गन्ना विकास समिति कार्यालय (Anoopshahr Cane Society) से संपर्क कर फॉर्म नंबर-3 भरकर डेटा अपडेट करा सकते हैं।

### Q3. अनूपशहर चीनी मिल में पेराई सत्र 2026-27 कब शुरू होगा?
सरकार द्वारा स्वीकृत अर्ली क्रशिंग प्लान के तहत अनूपशहर चीनी मिल में पेराई 15 अक्टूबर से 20 अक्टूबर 2026 के बीच शुरू हो जाएगी।

### Q4. अनूपशहर मिल का हेल्पलाइन नंबर क्या है?
गन्ना पर्ची या भुगतान से जुड़ी किसी भी समस्या के लिए किसान भाई राज्यस्तरीय टोल-फ्री हेल्पलाइन नंबर **`1800-121-3203`** पर 24 घंटे कॉल कर सकते हैं।

---

*अनूपशहर चीनी मिल, बुलंदशहर गन्ना पर्ची, eGanna App अपडेट और चीनी मिल समाचारों की हर प्रामाणिक रिपोर्ट के लिए [CaneUp.xyz](/) से जुड़े रहें!*
"""

with open(post_file, 'w', encoding='utf-8') as f:
    f.write(article_content)

print(f"Successfully updated Anoopshahr Mill Article with 453 villages & live search box!")
