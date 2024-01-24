-- Table: public.funding

-- DROP TABLE IF EXISTS public.funding;

CREATE TABLE IF NOT EXISTS public.funding
(
    funding_id uuid NOT NULL,
    total_funding text COLLATE pg_catalog."default" NOT NULL,
    funding_rounds bigint NOT NULL,
    lead_investors bigint NOT NULL,
    org_name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT funding_pkey PRIMARY KEY (funding_id),
    CONSTRAINT funding_org_name_fkey FOREIGN KEY (org_name)
        REFERENCES public.organization (org_name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.funding
    OWNER to root;