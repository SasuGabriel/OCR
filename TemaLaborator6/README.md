Disclaimer: Output-urile "Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Parser.xml" și "Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi_Tagger.xml" sunt obținute dintr-un tagger și un parser al documentului "Camil Petrescu - Ultima noapte de dragoste, intaia noapte de razboi.txt" astfel: 
Aici este pos tager-ul: https://www.dropbox.com/s/74gl7ubh3s10mcv/bin_PosRo.zip?dl=0

Se apeleaza, aproximativ, astfel:

HybridPOStagger tagger = new HybridPOStagger(new FileInputStream(args[0]), new FileInputStream(args[1]), new FileInputStream(args[2]), rules); // vezi ce sunt args in .bat

Document doc = tagger.tagTextXmlDetailed_en(sb.toString());

Aici e parserul: https://www.dropbox.com/s/fbr7glgv9yz44sy/bin_FdgParserRo.zip?dl=0

***Acesta e de fapt Malt parser cuplat cu o conversie a inputului din xml in conll si inapoi. Dar din cate retin nu ofera parserul ca un object pe care sa il mentii in memorie si sa il refolosesti… e mai mult un script in care toate se intampla la un loc. Dar e util sa vezi cum se foloseste malt si cum s-ar face conversia inputului si al outputului.*** Aici este codul sursa: https://www.dropbox.com/s/nt5uxc8ul97q522/MaltParseTaggedXml.java?dl=0.

*** A se vedea cu ce parametri e apelat parse_taggedXml.bat ***
