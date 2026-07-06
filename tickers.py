import yfinance as yf
import pandas as pd


# Updated 6.7.2026
tickers = {
  "ACG1V.HE": {
    "name": "Aspocomp Group",
    "sector": "Technology"
  },
  "AFAGR.HE": {
    "name": "Afarak Group",
    "sector": "Materials"
  },
  "AKTIA.HE": {
    "name": "Aktia Pankki",
    "sector": "Financials"
  },
  "ALBAV.HE": {
    "name": "Ålandsbanken A",
    "sector": "Financials"
  },
  "ALBBV.HE": {
    "name": "Ålandsbanken B",
    "sector": "Financials"
  },
  "ALMA.HE": {
    "name": "Alma Media",
    "sector": "Communication Services"
  },
  "ANORA.HE": {
    "name": "Anora Group",
    "sector": "Consumer Discretionary"
  },
  "APETIT.HE": {
    "name": "Apetit",
    "sector": "Consumer Discretionary"
  },
  "ASPO.HE": {
    "name": "Aspo",
    "sector": "Industrials"
  },
  "ATRAV.HE": {
    "name": "Atria",
    "sector": "Consumer Discretionary"
  },
  "AUROORA.HE": {
    "name": "Auroora Group",
    "sector": "Industrials"
  },
  "BIOBV.HE": {
    "name": "Biohit B",
    "sector": "Healthcare"
  },
  "BITTI.HE": {
    "name": "Bittium",
    "sector": "Technology"
  },
  "BOREO.HE": {
    "name": "Boreo",
    "sector": "Industrials"
  },
  "CAPMAN.HE": {
    "name": "CapMan",
    "sector": "Financials"
  },
  "CONSTI.HE": {
    "name": "Consti",
    "sector": "Industrials"
  },
  "CTH1V.HE": {
    "name": "Componenta",
    "sector": "Industrials"
  },
  "CTY1S.HE": {
    "name": "Citycon",
    "sector": "Real Estate"
  },
  "DETEC.HE": {
    "name": "Detection Technology",
    "sector": "Technology"
  },
  "DIGIA.HE": {
    "name": "Digia",
    "sector": "Technology"
  },
  "DIGIGR.HE": {
    "name": "Digitalist Group",
    "sector": "Technology"
  },
  "DOV1V.HE": {
    "name": "Dovre Group",
    "sector": "Industrials"
  },
  "EASOR.HE": {
    "name": "Easor",
    "sector": "Industrials"
  },
  "EEZY.HE": {
    "name": "Eezy",
    "sector": "Industrials"
  },
  "ELEAV.HE": {
    "name": "Elecster",
    "sector": "Industrials"
  },
  "ELISA.HE": {
    "name": "Elisa",
    "sector": "Communication Services"
  },
  "ENENTO.HE": {
    "name": "Enento Group",
    "sector": "Industrials"
  },
  "EQV1V.HE": {
    "name": "eQ",
    "sector": "Financials"
  },
  "ERIBR.HE": {
    "name": "Ericsson B",
    "sector": "Technology"
  },
  "ESENSE.HE": {
    "name": "Enersense International",
    "sector": "Industrials"
  },
  "ETTE.HE": {
    "name": "Etteplan",
    "sector": "Technology"
  },
  "EVLI.HE": {
    "name": "Evli",
    "sector": "Financials"
  },
  "EXEL.HE": {
    "name": "Exel Composites",
    "sector": "Industrials"
  },
  "FIA1S.HE": {
    "name": "Finnair",
    "sector": "Industrials"
  },
  "FORTUM.HE": {
    "name": "Fortum",
    "sector": "Energy"
  },
  "FRAMERY.HE": {
    "name": "Framery Group",
    "sector": "Industrials"
  },
  "FSECURE.HE": {
    "name": "F-Secure",
    "sector": "Technology"
  },
  "FSKRS.HE": {
    "name": "Fiskars",
    "sector": "Consumer Discretionary"
  },
  "GLA1V.HE": {
    "name": "Glaston",
    "sector": "Industrials"
  },
  "GOFORE.HE": {
    "name": "Gofore",
    "sector": "Technology"
  },
  "GRK.HE": {
    "name": "GRK Infra",
    "sector": "Industrials"
  },
  "HARVIA.HE": {
    "name": "Harvia",
    "sector": "Consumer Discretionary"
  },
  "HEALTH.HE": {
    "name": "Nightingale Health",
    "sector": "Healthcare"
  },
  "HIAB.HE": {
    "name": "Hiab",
    "sector": "Industrials"
  },
  "HKFOODS.HE": {
    "name": "HKFoods",
    "sector": "Consumer Discretionary"
  },
  "HONBS.HE": {
    "name": "Honkarakenne",
    "sector": "Real Estate"
  },
  "HUH1V.HE": {
    "name": "Huhtamäki",
    "sector": "Industrials"
  },
  "ICP1V.HE": {
    "name": "Incap",
    "sector": "Technology"
  },
  "ILKKA.HE": {
    "name": "Ilkka",
    "sector": "Communication Services"
  },
  "INVEST.HE": {
    "name": "Investors House",
    "sector": "Financials"
  },
  "IQMX.HE": {
    "name": "IQM",
    "sector": "Technology"
  },
  "KALMAR.HE": {
    "name": "Kalmar",
    "sector": "Industrials"
  },
  "KAMUX.HE": {
    "name": "Kamux",
    "sector": "Consumer Discretionary"
  },
  "KCR.HE": {
    "name": "Konecranes",
    "sector": "Industrials"
  },
  "KELAS.HE": {
    "name": "Kesla",
    "sector": "Industrials"
  },
  "KEMIRA.HE": {
    "name": "Kemira",
    "sector": "Materials"
  },
  "KEMPOWR.HE": {
    "name": "Kempower",
    "sector": "Industrials"
  },
  "KESKOA.HE": {
    "name": "Kesko A",
    "sector": "Consumer Discretionary"
  },
  "KESKOB.HE": {
    "name": "Kesko B",
    "sector": "Consumer Discretionary"
  },
  "KHG.HE": {
    "name": "KH Group",
    "sector": "Industrials"
  },
  "KNEBV.HE": {
    "name": "KONE",
    "sector": "Industrials"
  },
  "KOSKI.HE": {
    "name": "Koskisen",
    "sector": "Materials"
  },
  "KREATE.HE": {
    "name": "Kreate Group",
    "sector": "Industrials"
  },
  "KSL.HE": {
    "name": "Keskisuomalainen",
    "sector": "Communication Services"
  },
  "LAMOR.HE": {
    "name": "Lamor Corporation",
    "sector": "Industrials"
  },
  "LASTIK.HE": {
    "name": "Lassila & Tikanoja",
    "sector": "Industrials"
  },
  "LEHTO.HE": {
    "name": "Lehto Group",
    "sector": "Industrials"
  },
  "LINDEX.HE": {
    "name": "Lindex Group",
    "sector": "Consumer Discretionary"
  },
  "LUMO.HE": {
    "name": "Lumo Kodit",
    "sector": "Real Estate"
  },
  "LUOTEA.HE": {
    "name": "Luotea",
    "sector": "Real Estate"
  },
  "MANTA.HE": {
    "name": "Mandatum",
    "sector": "Financials"
  },
  "MARAS.HE": {
    "name": "Martela",
    "sector": "Industrials"
  },
  "MEKKO.HE": {
    "name": "Marimekko",
    "sector": "Consumer Discretionary"
  },
  "METSA.HE": {
    "name": "Metsä Board A",
    "sector": "Materials"
  },
  "METSB.HE": {
    "name": "Metsä Board B",
    "sector": "Materials"
  },
  "METSO.HE": {
    "name": "Metso",
    "sector": "Industrials"
  },
  "MUSTI.HE": {
    "name": "Musti Group",
    "sector": "Consumer Discretionary"
  },
  "NDA-FI.HE": {
    "name": "Nordea",
    "sector": "Financials"
  },
  "NESTE.HE": {
    "name": "Neste",
    "sector": "Energy"
  },
  "NLG1V.HE": {
    "name": "Nurminen Logistics",
    "sector": "Industrials"
  },
  "NOHO.HE": {
    "name": "NoHo Partners",
    "sector": "Consumer Discretionary"
  },
  "NOKIA.HE": {
    "name": "Nokia",
    "sector": "Technology"
  },
  "OLVAS.HE": {
    "name": "Olvi A",
    "sector": "Consumer Discretionary"
  },
  "OMASP.HE": {
    "name": "Oma Säästöpankki",
    "sector": "Financials"
  },
  "OPTOMED.HE": {
    "name": "Optomed",
    "sector": "Healthcare"
  },
  "ORIOLA.HE": {
    "name": "Oriola",
    "sector": "Healthcare"
  },
  "ORNAV.HE": {
    "name": "Orion A",
    "sector": "Healthcare"
  },
  "ORNBV.HE": {
    "name": "Orion B",
    "sector": "Healthcare"
  },
  "ORTHEX.HE": {
    "name": "Orthex",
    "sector": "Consumer Discretionary"
  },
  "OUT1V.HE": {
    "name": "Outokumpu",
    "sector": "Materials"
  },
  "OVARO.HE": {
    "name": "Ovaro Kiinteistösijoitus",
    "sector": "Real Estate"
  },
  "PAMPALO.HE": {
    "name": "Endomines",
    "sector": "Materials"
  },
  "PIHLIS.HE": {
    "name": "Pihlajalinna",
    "sector": "Healthcare"
  },
  "PNA1V.HE": {
    "name": "Panostaja",
    "sector": "Financials"
  },
  "PON1V.HE": {
    "name": "Ponsse",
    "sector": "Industrials"
  },
  "POSTI.HE": {
    "name": "Posti Group",
    "sector": "Industrials"
  },
  "PUUILO.HE": {
    "name": "Puuilo",
    "sector": "Consumer Discretionary"
  },
  "QPR1V.HE": {
    "name": "QPR Software",
    "sector": "Technology"
  },
  "QTCOM.HE": {
    "name": "Qt Group",
    "sector": "Technology"
  },
  "RAIKV.HE": {
    "name": "Raisio K",
    "sector": "Consumer Discretionary"
  },
  "RAIVV.HE": {
    "name": "Raisio V",
    "sector": "Consumer Discretionary"
  },
  "RAP1V.HE": {
    "name": "Rapala VMC",
    "sector": "Consumer Discretionary"
  },
  "RAUTE.HE": {
    "name": "Raute",
    "sector": "Industrials"
  },
  "REAKTOR.HE": {
    "name": "Reaktor",
    "sector": "Technology"
  },
  "REBL.HE": {
    "name": "Rebl Group",
    "sector": "Consumer Discretionary"
  },
  "REG1V.HE": {
    "name": "Revenio Group",
    "sector": "Healthcare"
  },
  "REKA.HE": {
    "name": "Reka Industrial",
    "sector": "Industrials"
  },
  "RELAIS.HE": {
    "name": "Relais Group",
    "sector": "Consumer Discretionary"
  },
  "REMEDY.HE": {
    "name": "Remedy Entertainment",
    "sector": "Technology"
  },
  "ROBIT.HE": {
    "name": "Robit",
    "sector": "Industrials"
  },
  "SAGCV.HE": {
    "name": "Saga Furs",
    "sector": "Consumer Discretionary"
  },
  "SAMPO.HE": {
    "name": "Sampo",
    "sector": "Financials"
  },
  "SANOMA.HE": {
    "name": "Sanoma",
    "sector": "Communication Services"
  },
  "SAVOX.HE": {
    "name": "Savox Communications",
    "sector": "Technology"
  },
  "SCANFL.HE": {
    "name": "Scanfil",
    "sector": "Technology"
  },
  "SIILI.HE": {
    "name": "Siili Solutions",
    "sector": "Technology"
  },
  "SITOWS.HE": {
    "name": "Sitowise Group",
    "sector": "Industrials"
  },
  "SOLTEQ.HE": {
    "name": "Solteq",
    "sector": "Technology"
  },
  "SOSI1.HE": {
    "name": "Sotkamo Silver",
    "sector": "Materials"
  },
  "SRV1V.HE": {
    "name": "SRV Yhtiöt",
    "sector": "Industrials"
  },
  "SSABAH.HE": {
    "name": "SSAB A",
    "sector": "Materials"
  },
  "SSABBH.HE": {
    "name": "SSAB B",
    "sector": "Materials"
  },
  "SSH1V.HE": {
    "name": "SSH Communications",
    "sector": "Technology"
  },
  "STEAV.HE": {
    "name": "Stora Enso A",
    "sector": "Materials"
  },
  "STERV.HE": {
    "name": "Stora Enso R",
    "sector": "Materials"
  },
  "SUY1V.HE": {
    "name": "Suominen",
    "sector": "Industrials"
  },
  "TAALA.HE": {
    "name": "Taaleri",
    "sector": "Financials"
  },
  "TALLINK.HE": {
    "name": "Tallink",
    "sector": "Consumer Discretionary"
  },
  "TELIA1.HE": {
    "name": "Telia Company",
    "sector": "Communication Services"
  },
  "TEM1V.HE": {
    "name": "Tecnotree",
    "sector": "Technology"
  },
  "TIETO.HE": {
    "name": "TietoEVRY",
    "sector": "Technology"
  },
  "TLT1V.HE": {
    "name": "Teleste",
    "sector": "Technology"
  },
  "TNOM.HE": {
    "name": "Talenom",
    "sector": "Industrials"
  },
  "TOIVO.HE": {
    "name": "Toivo Group",
    "sector": "Real Estate"
  },
  "TOKMAN.HE": {
    "name": "Tokmanni",
    "sector": "Consumer Discretionary"
  },
  "TRH1V.HE": {
    "name": "Trainers' House",
    "sector": "Technology"
  },
  "TTALO.HE": {
    "name": "Terveystalo",
    "sector": "Healthcare"
  },
  "TULAV.HE": {
    "name": "Tulikivi",
    "sector": "Industrials"
  },
  "TYRES.HE": {
    "name": "Nokian Renkaat",
    "sector": "Consumer Discretionary"
  },
  "UNITED.HE": {
    "name": "United Bankers",
    "sector": "Financials"
  },
  "UPM.HE": {
    "name": "UPM-Kymmene",
    "sector": "Materials"
  },
  "VAIAS.HE": {
    "name": "Vaisala",
    "sector": "Technology"
  },
  "VALMT.HE": {
    "name": "Valmet",
    "sector": "Industrials"
  },
  "VERK.HE": {
    "name": "Verkkokauppa.com",
    "sector": "Consumer Discretionary"
  },
  "VIK1V.HE": {
    "name": "Viking Line",
    "sector": "Consumer Discretionary"
  },
  "VINCIT.HE": {
    "name": "Vincit",
    "sector": "Technology"
  },
  "WETTERI.HE": {
    "name": "Wetteri",
    "sector": "Consumer Discretionary"
  },
  "WRT1V.HE": {
    "name": "Wärtsilä",
    "sector": "Industrials"
  },
  "WUF1V.HE": {
    "name": "Wulff-Yhtiöt",
    "sector": "Industrials"
  },
  "YIT.HE": {
    "name": "YIT",
    "sector": "Industrials"
  }
}